var div_com = document.getElementById("div_comment");
var resp_com = document.getElementById("resp_comment");
resp_com.onclick = function() {
    div_com.style.display = "block";
}
var exit_block = document.getElementById("exit_div");
exit_block.onclick = function() {
    div_com.style.display = "none";
}