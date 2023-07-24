$('.delete-student').click(function () {
      console.log('Deleteeeeeeeee');
      var csrfToken = $("input[name='csrfmiddlewaretoken']").val();
      $.ajax({
        url: `/delete_student/${$(this).val()}/`,
        type: 'POST',
        beforeSend: function (xhr) {
          xhr.setRequestHeader("X-CSRFToken", csrfToken);
        },
        success: function () {
          alert("Student deleted");
          console.log("Student deleted");
          location.reload();
        },
        error: function () {
          alert('Error deleting student');
        }
      });
      
    })