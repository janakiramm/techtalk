function main(params) {

  return new Promise(function(resolve, reject) {
    console.log(params.order);
    console.log(params.manager);

    if (!params.order) {
      console.error('Order parameter not set.');
      reject({
        'error': 'Order parameter not set.'
      });
      return;
    } else {
      var message = 'Order worth $' + params.order + ' is closed by ' + params.manager;
      console.log(message);
      resolve({
        change: message
      });
      return;
    }

  });

}
