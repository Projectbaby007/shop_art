const menuBtn = document.querySelector(".menu-btn");
const navbar = document.querySelector(".navbar")

menuBtn.addEventListener("click", () =>{
    menuBtn.classList.toggle("active");
    navbar.classList.toggle("active");
});