document.addEventListener('DOMContentLoaded', function() {
    const typeSelector = document.getElementById('type-selector');
    const activityFields = document.getElementById('activity-fields');
    let picker = null;

    typeSelector.addEventListener('change', function() {
        if (this.value === 'activity') {
            activityFields.style.display = 'block';
            
            // Only create the picker if it doesn't exist yet
            if (!picker) {
                picker = new DateTimePicker('#example', {
                    minuteStep: 5,
                    startOfWeek: 0,
                    defaultHour: 9,
                    initial: new Date(),
                    format: (date) => {
                        const p = (n) => String(n).padStart(2, '0');
                        return `${p(date.getDate())}-${p(date.getMonth() + 1)}-${date.getFullYear()}- ${p(date.getHours())}:${p(date.getMinutes())}`;
                    }
                });
            }
        } else {
            activityFields.style.display = 'none';
        }
    });
});