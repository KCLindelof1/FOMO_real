$(function(context) {
    return function() {
        var container = $('#s1container')
        console.log(container)
    //     $.ajax({
    //         url: 'http://www.byu.edu/'
    //     })
    // //    or
        container.load('http://www.byu.edu/')

    }
}(DMP_CONTEXT.get()))
