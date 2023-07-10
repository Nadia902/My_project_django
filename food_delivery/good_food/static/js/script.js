let slides = document.querySelectorAll(".program-group__el");

for(let i = 0; i< slides.length; i++) {
    slides[i].addEventListener('click', () => {
        clearActiveClasses()
        slides[i].classList.add('active');
    });
}

function clearActiveClasses(){
    for(let i = 0; i< slides.length; i++) {
        slides[i].classList.remove('active');
    }
}

let slides_two = document.querySelectorAll(".f-column");

for(let i = 0; i< slides_two.length; i++) {
    slides_two[i].addEventListener('click', () => {
        clearActiveClass()
        slides_two[i].classList.add('active_two');
    });
}

function clearActiveClass(){
    for(let i = 0; i< slides_two.length; i++) {
        slides_two[i].classList.remove('active_two');
    }
}