var myButton = document.getElementById("myButton");
var myOption = document.getElementById("myOption");
myButton.addEventListener("click", function(){
if (myOption.style.display === "none") {
    myOption.style.display = "block";
} else {
    myOption.style.display = "none";
}
});
