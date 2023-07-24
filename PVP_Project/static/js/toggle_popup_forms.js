$('#create_new_category_btn').click(function(){
  $('#category-form-container').toggle();
  $('#subject-form-container').css('display', 'none');
  $('#student-form-container').css('display', 'none');
})
  

$('#create_new_subject_btn').click(function(){
  $('#subject-form-container').toggle();
  $('#category-form-container').css('display', 'none');
  $('#student-form-container').css('display', 'none');
  })

$('#create_new_student_btn').click(function(){
  $('#student-form-container').toggle();
  $('#category-form-container').css('display', 'none');
  $('#subject-form-container').css('display', 'none');
})
  

$('#change_test_conditions_btn').click(function () {
  $('#test-conditions-form-container').toggle();
})

$('#close_update_test_conditions_form').click(function () {
  $('#test-conditions-form-container').toggle();
})

$('#close_category_form').click(function () {
    $('#category-form-container').toggle();
})

$('#close_student_form').click(function () {
    $('#student-form-container').toggle();
})
$('#close_subject_form').click(function () {
    $('#subject-form-container').toggle();
})