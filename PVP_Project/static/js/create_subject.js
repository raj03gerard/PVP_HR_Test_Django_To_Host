$(document).ready(function () { 

    $('#subject_form').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function () { 
                console.log("Subject sent");
            },
            error: function () {
                console.log('Error submitting subject form.');
            }
        });
        location.reload();
    })
});