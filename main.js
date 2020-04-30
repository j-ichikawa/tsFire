javascript:(async function () {
    // variables
    const startDate = 1;
    const endDate = 31;
    const startTime = '09:30';
    const endTime = '18:00';
    const waitMSec = 1000;

    // weekly report end time
    let dt = new Date(0, 0, 0, Number(endTime.slice(0, 2)), Number(endTime.slice(-2)));
    dt.setMinutes(dt.getMinutes() + 30);
    const weeklyReportEndTime = dt.getHours().toString() + ':' + dt.getMinutes().toString();

    for (let i = startDate; i <= endDate; i++) {
        const dt = new Date();
        const date = dt.getFullYear().toString() + '-' + (dt.getMonth() + 1).toString().padStart(2, '0') + '-' +
            Number(i).toString().padStart(2, '0');
        const isFriday = document.getElementById('dateRow' + date).cells[1].innerText == '金';
        const time = document.getElementById('ttvTimeSt' + date);
        if (time) {
            // input date
            time.click();
            document.getElementById('startTime').value = startTime;

            if (isFriday) {
                document.getElementById('endTime').value = weeklyReportEndTime;
                document.getElementById('startOut1').value = endTime;
                document.getElementById('endOut1').value = weeklyReportEndTime;
            } else {
                document.getElementById('endTime').value = endTime;
            }

            document.getElementById('dlgInpTimeOk').click();

            await new Promise(resolve => setTimeout(resolve, waitMSec));

            // input note
            if (isFriday) {
                document.getElementById('dailyNoteIcon' + date).click();
                document.getElementById('dialogNoteText2').value = '週報作成 0:30h';
                document.getElementById('dialogNoteOk').click();

                await new Promise(resolve => setTimeout(resolve, waitMSec));
            }
        }
    }
})();
