// Default javascript
//
// (function(context) {
//
//     // utc_epoch comes from index.py
//     console.log('Current epoch in UTC is ' + context.utc_epoch);
//
// })(DMP_CONTEXT.get());


$(function(context) {
    return function() {
        //code here
        $('#catalog').load("catalog/index.products/" + context.category + "/1/")

    //
    }
}(DMP_CONTEXT.get()))
