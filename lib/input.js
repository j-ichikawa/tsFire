(async function () {
    "use strict";
    // variables
    const startDate = 1;
    const endDate = 31;
    const waitMSec = 2500;
    const kinmu_models = JSON.parse('KINMU_MODELS')

    for (let i = startDate; i <= endDate; i++) {
        const dt = new Date();
        const date = dt.getFullYear().toString() + '-' + (dt.getMonth() + 1).toString().padStart(2, '0') + '-' +
            Number(i).toString().padStart(2, '0');
        const isFriday = document.getElementById('dateRow' + date).cells[1].innerText === '金';
        const time = document.getElementById('ttvTimeSt' + date);
        if (time) {
            const kinmu = kinmu_models[Number(time.id.substr(-2))]
            // input date
            time.click();
            document.getElementById('startTime').value = kinmu[0];

            // for weeklyReport
            if (isFriday) {
                let dt = new Date(0, 0, 0, Number(kinmu[1].slice(0, 2)), Number(kinmu[1].slice(-2)));
                dt.setMinutes(dt.getMinutes() + 30);
                const weeklyReportEndTime = dt.getHours().toString() + ':' + dt.getMinutes().toString();

                document.getElementById('endTime').value = weeklyReportEndTime;
                document.getElementById('startOut1').value = kinmu[1];
                document.getElementById('endOut1').value = weeklyReportEndTime;
            } else {
                document.getElementById('endTime').value = kinmu[1];
            }

            // clear break time
            if (kinmu[2] === '0') {
                document.getElementById('startRest1').value = '';
                document.getElementById('endRest1').value = '';
            }

            document.getElementById('dlgInpTimeOk').click();

            await new Promise(resolve => setTimeout(resolve, waitMSec));

            // input note
            if (isFriday) {
                document.getElementById('dailyNoteIcon' + date).click();
                const weeklyReportNote = '週報作成 0:30h'
                if (!document.getElementById('dialogNoteText2').value.includes(weeklyReportNote)) {
                    document.getElementById('dialogNoteText2').value += weeklyReportNote
                }
                document.getElementById('dialogNoteOk').click();

                await new Promise(resolve => setTimeout(resolve, waitMSec));
            }
        }
    }

    console.log('done.');
})();
