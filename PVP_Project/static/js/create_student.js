$(document).ready(function () { 

    $('#create_student_form').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function () { 
                console.log("Student data sent");
            },
            error: function () {
                console.log('Error submitting student form.');
            }
        }); 
        location.reload();
        console.log("PLEASE RELOAD!!!");
    })
});