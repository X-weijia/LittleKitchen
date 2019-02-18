$(function () {
    let a=$('.Classification li')
    let b=$('.specific li')
    let c=$('.style')
    a.each(function (i) {
        $(this).click(function () {
            b.css('z-index','2').eq(i).css('z-index','99')
            c.css('background','#f8f0e2').eq(i).css('background','#fcc23b')
        })
    })
});
