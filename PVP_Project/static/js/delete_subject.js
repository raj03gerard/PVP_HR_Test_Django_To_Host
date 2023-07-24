$('.delete_subject').click(function (){
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    $.ajax({
            url: `/delete_subject/${$(this).val()}/`,
            type: 'POST',
            beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
             },
            success: function (response) { 
                alert(response['message']);
            },
            error: function (response) {
                alert('Error deleting subject');
            }
    });
    location.reload();
})


