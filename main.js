// inicializador do swiper
const swiper = new Swiper('.swiper', {

    //pra experimentar depois: trocar o flex do container__jogos pra um slider que mostra a quantidade de jogos que couberem na tela
/*
    // Default parameters
    slidesPerView: 1,
    spaceBetween: 10,
    // Responsive breakpoints
    breakpoints: {
        // when window width is >= 320px
        320: {
        slidesPerView: 2,
        spaceBetween: 20
        },
        // when window width is >= 480px
        480: {
        slidesPerView: 3,
        spaceBetween: 30
        },
        // when window width is >= 640px
        640: {
        slidesPerView: 4,
        spaceBetween: 40
        }
    }
*/

    // Optional parameters
    direction: 'horizontal',
    loop: true,
  
    // If we need pagination
    pagination: {
      el: '.swiper-pagination',
    },
  
    // Navigation arrows
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  
});

//ativador do menu lateral mobile
function toggleMenu()
{
    const botao = document.querySelectorAll('.linha1, .linha2, .linha3, .barranav');

    for(let i = 0; i < botao.length; i++)
    {
        botao[i].classList.toggle('menuaberto');
    }
}

//tocador do som do rodape
function tocaHONK()
{
    const audio = document.querySelector('audio');
    audio.play();
}
