$(function(context){
    return function() {

        //give each image a similar class, then say
        // $('.product_images_detail').mouseenter(function(){
        //     console.log($(this))
        //
        //     $('.product_images_main').attr()'#currentPage").text(context.pNum)
        // });

        //use img urls method (do a for loop?)
        //load first image by default
        //either create all graphics an
        //keep same img tag, but change src of this tag
        //get src of the img that the mouse hovers over and set it to the big picture.

        $('.product_images_detail').on('mouseenter', function() {
            var imageSrc = $('.product_images_main');
            imageSrc[0].innerHTML = this.innerHTML;
        });

    // $(function(){
    //     $('.imgThumbs').on('mouseenter', function() {
    //         var thumbSrc = $('#mainImage');
    //         thumbSrc[0].innerHTML = this.innerHTML;
    //     });
    // });

    }
}(DMP_CONTEXT.get()));
