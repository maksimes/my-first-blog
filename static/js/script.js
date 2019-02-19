$("#resp_comment").click(function() {
    $("#div_comment").css({"display":"block"});
});
// появление блока комментария к постам при нажатии кнопки "ответить"


$("#exit_div").click(function() {
    $("#div_comment").css({"display":"none"});
});
// скрытие блока комментария в момент нажатия на крестик


$(".comments").load("comments_ajax/");
// подгрузка комментариев без перезагрузки страницы


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
//лайки-дизлайки при клике на сердечко


$("#exit_feedback").click(function() {
    $("#feedback_block").animate({bottom: '-410'}, 1000);
    $("#exit_feedback").css({display: "none"})
    $('#fb_mytext').text("напишите мне!");
});
// сдвиг формы обратной связи вниз при клике на крестик


$("#fb_title").click(function() {
    $("#feedback_block").animate({bottom: '0'}, 1000);
    $("#exit_feedback").css({display: "block"})
});
// появление блока обратной связи снизу при клике на его зоголовок


$('#feedback_form').submit(function(){
    $.ajax({
        headers: {"X-CSRFToken": $.cookie("csrftoken")},
        data: $(this).serialize(),
        type: "POST",
        url: "feedback/",
        success: function(response) {
            $('#fb_mytext').text(response);
            $("#feedback_form").each(function(){
            this.reset();
            });

        },
        error: function(rs, e) {
           alert(rs.responseText);
        }
    });
    return false;
});
// отправка обратной связи на почту при нажатии кнопки "отправить"


$('#add_comment').submit(function(){
    $.ajax({
        headers: {"X-CSRFToken": $.cookie("csrftoken")},
        data: $(this).serialize(),
        type: "POST",
        url: "add_comment/",
        success: function(response) {
            $("#div_comment").css({"display":"none"});
            $(".comments").load("comments_ajax/");
            $("#add_comment").each(function(){
            this.reset();
            });

        },
        error: function(rs, e) {
           alert(rs.responseText);
        }
    });
    return false;
});
//создание комментария к посту