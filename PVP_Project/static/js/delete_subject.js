$('.delete_subject').click(function (){
    var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
    message="error"
    $.ajax({
            url: `/delete_subject/${$(this).val()}/`,
            type: 'POST',
            beforeSend: function(xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrfToken);
             },
        success: function (response) { 
                message= response['message']
                alert(response['message']);
                location.reload();
            },
            error: function (response) {
                
                alert('Error deleting subject');
            }
    });
    
    
})


