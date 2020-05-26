import json
import re
from typing import List, Pattern

from pdfminer.high_level import extract_text


def extract_kinmu_model_json(pdf_path: str) -> str:
    texts: List[str] = [_ for _ in extract_text(pdf_path, laparams=None).splitlines() if _]

    pattern: Pattern[str] = re.compile(r'\d+\s')
    start_times: List[str] = [_ for _ in texts if pattern.match(_)]

    work_days_number: int = len(list(filter(lambda x: len(x) > 4, start_times)))

    error_indexes = __get_error_line_indexes(start_times)

    start_times_last_index: int = texts.index(start_times[-1])

    end_times: List[str] = [_ for _ in texts[start_times_last_index + 1:start_times_last_index + 1 + work_days_number]]
    # error correction
    end_times = [_ for _ in end_times if ':' in _]
    [end_times.insert(_, '18:00') for _ in error_indexes]

    breaks_start_index: int = start_times_last_index + len(end_times) - 1
    breaks: List[str] = [_ for _ in texts[breaks_start_index:breaks_start_index + work_days_number]]
    # error correction
    breaks = [_ for _ in breaks if ':' not in _]
    [breaks.insert(_, '1') for _ in error_indexes]

    kinmu_models = {}
    work_days_index = 0
    for _ in start_times:
        if ':' in _:
            kinmu_models[int(_.split()[0])] = (_.split()[-1], end_times[work_days_index], breaks[work_days_index])
            work_days_index += 1

    return json.dumps(kinmu_models)


def __get_error_line_indexes(start_times):
    """
    return indexes elements with no date on both neighbors
    :param start_times:
    :return:
    """
    is_day_before_no_date = True
    indexes = []
    for i, t in enumerate(start_times):
        # is not end element?
        if i != len(start_times) - 1:
            if ':' in start_times[i]:
                # is single line?
                if is_day_before_no_date and ':' not in start_times[i + 1]:
                    indexes.append(i)
                is_day_before_no_date = False
            else:
                is_day_before_no_date = True
        else:
            # end element
            if is_day_before_no_date and ':' in start_times[i]:
                indexes.append(i)

    return indexes
