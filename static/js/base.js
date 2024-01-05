"use strict";
document.addEventListener("DOMContentLoaded", function (event) {
    let navMenuCheckBox = document.querySelector(".menu-checkbox");
    let navbar = document.querySelector(".navbar");
    function showMenu() {
        if (navMenuCheckBox.checked) {
            navbar.style.height = '150px';
            return;
        }
        navbar.style.height = '50px';
    }
    navMenuCheckBox.addEventListener('click', showMenu);
});
