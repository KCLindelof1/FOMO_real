$(function(context) {
    return function() {
        var container = $('#s1container')
        // console.log(container)
    //     $.ajax({
    //         url: 'http://www.byu.edu/'
    //     })
    // //    or
        container.load('/catalog/s1demo.inner/')

    }
}(DMP_CONTEXT.get()))
