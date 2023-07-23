$('.delete_subject').click(function (){
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
            url: `/delete_subject/${$(this).val()}/`,
            type: 'POST',
            beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
             },
            success: function () { 
                console.log("Subject deleted");
            },
            error: function () {
                console.log('Error deleting subject');
            }
    });
    location.reload();
})


