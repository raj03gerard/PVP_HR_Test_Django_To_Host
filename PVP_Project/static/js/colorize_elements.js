
$('document').ready(function () {
    $.ajax({
            url: 'get_default_colors',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                $('.category-field').each(function() {
                    var value = $(this).text().trim();
                    $(this).css("background-color",
                        response['categories'][value]
                        );
                        console.log(value)
                });
                console.log(response['categories']['ARTS'])
            },
            error: function(xhr, status, error) {
                
                console.error('Error:', status, error);
            }
    });
    
    $('.student-result').each(function () {
        var value = $(this).text().trim();
        if (value == 'PASS')
        {
            $(this).css("background-color",'green');
            $(this).css("color",'white');
        }
        else if (value == 'FAIL')
        {
            $(this).css("background-color",'red');
            $(this).css("color",'white');
        }
    })
})