$(document).ready(function() {
    // Function to set min and max time based on user selection
    function updateMinAndMaxTime() {
        var currentTime = new Date();
        var currentHour = currentTime.getHours();
        var currentMinute = currentTime.getMinutes();
        var currentTimeString = ('0' + currentHour).slice(-2) + ':' + ('0' + currentMinute).slice(-2); // Format current time as HH:MM

        // Set minimum time to 10:00 AM if the current time is before 10 AM
        if (currentHour < 10 || (currentHour === 10 && currentMinute === 0)) {
            $('#id_time').attr('min', '10:00');
        } else {
            $('#id_time').attr('min', currentTimeString);
        }

        // Set maximum time to 4:00 PM
        $('#id_time').attr('max', '16:00');
    }

    // Call the function if the element with id_time exists
    if ($('#id_time').length) {
        updateMinAndMaxTime();

        // Call the function whenever the time input value changes
        $('#id_time').on('input', function() {
            updateMinAndMaxTime();
        });
    }
});
