window.onload = function () {

    let stars = document.querySelector('#stars')
    let moon = document.getElementById('moon');
    let mountains_behind = document.getElementById('mountains_behind');
    let text = document.getElementById('text');
    let btn = document.getElementById('btn');
    let mountains_front = document.getElementById('mountains_front');

    window.addEventListener('scroll', function () {
        let val = window.scrollY;
        stars.style.left = val * 0.45 + 'px';
        moon.style.top = val * 1.15 + 'px';
        mountains_behind.style.top = val * 0.6 + 'px';
        mountains_front.style.top = val * 0 + 'px';
        btn.style.marginRight = val * 4 + 'px';
        text.style.marginRight = val * 4 + 'px';
    });


}
