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
          console.log("Student deleted");
        },
        error: function () {
          console.log('Error deleting student');
        }
      });
      location.reload();
    })