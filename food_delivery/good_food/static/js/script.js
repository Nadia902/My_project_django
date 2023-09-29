let slides = document.querySelectorAll(".program-group__el");
let eat = document.querySelectorAll(".eat_flex");
let prices = document.querySelector("#programTotal");

// при клике на кол-во каллорий добавляем класс: active
function clear(){
    for(let i = 0; i < slides.length; i++) {
        slides[i].addEventListener('click', () => {
            clearActiveClasses() // вызов функции удаления класса
            slides[i].classList.add('active')
        });
    }
}
// при клике на кол-во каллорий удаляем класс active у всех остальных каллорий
function clearActiveClasses(){
    for(let i = 0; i< slides.length; i++) {
        slides[i].classList.remove('active');
    }
}

clear() // вызов функции

// выводим блюда на экран по каллориям (при клике вызывается функция)
function light(){
    for(let i = 0; i < eat.length; i++) {
        eat[i].classList.add('eatnone2')  // добавляем всем класс для скрытия объектов
        }
    let li = document.querySelectorAll(".lightx")
    for(let j = 0; j < li.length; j++) {
        li[j].classList.remove('eatnone2') // удаляем класс у нужного нам элемента для его отображения
    }
    prices.textContent = 850;  // добавляем стоимость блюд
}

function normal(){
    for(let i = 0; i < eat.length; i++) {
        eat[i].classList.add('eatnone2')
        }
    let no = document.querySelectorAll(".normalx")
    for(let j = 0; j < no.length; j++) {
        no[j].classList.remove('eatnone2')
    }
    prices.textContent = 990;
}

function strong(){
    for(let i = 0; i < eat.length; i++) {
        eat[i].classList.add('eatnone2')
        }
    let st = document.querySelectorAll(".strongx")
    for(let j = 0; j < st.length; j++) {
        st[j].classList.remove('eatnone2')
    }
    prices.textContent = 1050;
}

function superstrong(){
    for(let i = 0; i < eat.length; i++) {
        eat[i].classList.add('eatnone2')
        }
    let su = document.querySelectorAll(".superstrongx")
    for(let j = 0; j < su.length; j++) {
        su[j].classList.remove('eatnone2')
    }
    prices.textContent = 1200;
}

function super1(){
    for(let i = 0; i < eat.length; i++) {
        eat[i].classList.add('eatnone2')
        }
    let sup = document.querySelectorAll(".superx")
    for(let j = 0; j < sup.length; j++) {
        sup[j].classList.remove('eatnone2')
    }
    prices.textContent = 1350;
}


// добавляем функционал для выбора блюд по дням недели
let food = document.querySelectorAll(".foodflex"); // получаем доступ для отображения блюд по дням недели
let column = document.querySelectorAll(".f-column"); // получаем доступ для активности выбранного дня недели на панеле

// при клике на день недели добавляем класс: active_two
function cleartwo(){
    for(let i = 0; i < column.length; i++) {
        column[i].addEventListener('click', () => {
            clearActiveClassestwo()  // вызов функции удаления класса
            column[i].classList.add('active_two')
        });
    }
}

function clearActiveClassestwo(){
    for(let i = 0; i< column.length; i++) {
        column[i].classList.remove('active_two');
    }
}

cleartwo()  // вызов самой функции

// вызов функций при клике по дням недели
function monday(){
    for(let i = 0; i < food.length; i++) {
        food[i].classList.add('eatnone')
        }
    let m = document.querySelectorAll(".monday")
    for(let j = 0; j < m.length; j++) {
        m[j].classList.remove('eatnone')
    }
}

function tuesday(){
    for(let i = 0; i < food.length; i++) {
        food[i].classList.add('eatnone')
        }
    let t = document.querySelectorAll(".tuesday")
    for(let j = 0; j < t.length; j++) {
        t[j].classList.remove('eatnone')
    }
}
function wednesday(){
    for(let i = 0; i < food.length; i++) {
        food[i].classList.add('eatnone')
        }
    let w = document.querySelectorAll(".wednesday")
    for(let j = 0; j < w.length; j++) {
        w[j].classList.remove('eatnone')
    }
}
function thursday(){
    for(let i = 0; i < food.length; i++) {
        food[i].classList.add('eatnone')}
    let h = document.querySelectorAll(".thursday")
    for(let j = 0; j < h.length; j++) {
        h[j].classList.remove('eatnone')
    }
}
function friday(){
    for(let i = 0; i < food.length; i++) {
        food[i].classList.add('eatnone')}
    let f = document.querySelectorAll(".friday")
    for(let j = 0; j < f.length; j++) {
        f[j].classList.remove('eatnone')
    }
}
function saturday(){
    for(let i = 0; i < food.length; i++) {
        food[i].classList.add('eatnone')}
    let t = document.querySelectorAll(".saturday")
    for(let j = 0; j < t.length; j++) {
        t[j].classList.remove('eatnone')
    }
}
function sunday(){
    for(let i = 0; i < food.length; i++) {
        food[i].classList.add('eatnone')}
    let d = document.querySelectorAll(".sunday")
    for(let j = 0; j < d.length; j++) {
        d[j].classList.remove('eatnone')
    }
}

