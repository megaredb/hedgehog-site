document.addEventListener("DOMContentLoaded", function(event) {
    let navMenuCheckBox: HTMLInputElement = document.querySelector(".menu-checkbox") as HTMLInputElement;
    let navbar: HTMLDivElement = document.querySelector(".navbar") as HTMLDivElement;

    function showMenu() {
        if (navMenuCheckBox.checked) {
            navbar.style.height = '150px';

            return;
        }

        navbar.style.height = '50px';
    }


    navMenuCheckBox.addEventListener('click', showMenu);
});
