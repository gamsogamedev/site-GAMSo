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
