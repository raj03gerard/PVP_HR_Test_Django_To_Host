$(document).ready(function () { 

    $('#category_form').submit(function (event) {
        event.preventDefault();
        var formData = $(this).serialize();

        $.ajax({
            url: $(this).attr('action'),
            type: 'POST',
            data: formData,
            success: function () { 
                console.log("Category sent");
                
            },
            error: function () {
                console.log('Error submitting category form.');
            }
        });
        location.reload();
    })
});