$("#resp_comment").click(function() {
    $("#div_comment").css({"display":"block"});
});

$("#exit_div").click(function() {
    $("#div_comment").css({"display":"none"});
});

$(".comments").load("comments_ajax/");


$('.like').click(function(){
    $.ajax({
        headers: {"X-CSRFToken": $.cookie("csrftoken")},
        type:"POST",
        url: "add_like/",
        data: {'postid': $(this).attr('name')},
        dataType: "json",
        success: function(response) {
            $('#like_count_'+response.post_id).text(response.likes_count);
        },
        error: function(rs, e) {
           alert(rs.responseText);
        }
    });
});
