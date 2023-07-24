$(document).ready(function () { 

    $('#create_student_form').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function (response) { 
                alert(response['message']);
                location.reload();
            },
            error: function () {
                console.log('Error submitting student form.');
            }
        }); 
        
        
        
    })
});

$('.subject-field').focus(function (){
    $(this).val("");
})

$('.subject-field').blur(function() {
        if ($(this).val() === '') {
            $(this).val('0');
        }
    });
