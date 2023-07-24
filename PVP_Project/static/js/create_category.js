$(document).ready(function () { 

    $('#category_form').submit(function (event) {
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
                console.log('Error submitting category form.');
            }
        });
        
    })
});