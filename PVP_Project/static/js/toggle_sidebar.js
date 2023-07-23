$('#collapse-sidebar-btn').click(function (){
    $('#right_sidebar').css('width', '0');
    $('#collapse-sidebar-btn').toggle();
    $('#expand-sidebar-btn').toggle();
    $('.section-contents').toggle();
})
$('#expand-sidebar-btn').click(function (){
    $('#right_sidebar').css('width', '450px');
    $('#collapse-sidebar-btn').toggle();
    $('#expand-sidebar-btn').toggle();
    $('.section-contents').toggle();
})