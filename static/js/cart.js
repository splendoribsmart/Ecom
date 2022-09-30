// console.log('Hello World');

var updateBtns = document.getElementsByClassName('update-cart');

// console.log(updateBtns)

for (let i of updateBtns) {
  i.addEventListener('click', function(){
    var productId = this.dataset.product;
    var action = this.dataset.action;
    console.log('productId:', productId, 'action:', action);

    console.log('User:', USER);
    if (USER === 'AnonymousUser') {
      console.log('User Is Not LoggedIn');
    } else {
      updateUserOrder(productId, action);
    }
  })
}

function updateUserOrder(productId, action){
  console.log('User Is LoggedIn, Sending Data...');

  let url = '/update_item/';

  fetch(url, {
    method : 'POST',
    headers : {
      'Content-Type' : 'application/json',
      'X-CSRFToken' : csrftoken,
    },
    body : JSON.stringify({'productId' : productId, 'action' : action})
  })

  .then((response) => {
    return response.json();
  })
  .then((data) => {
    location.reload()
    console.log('data:', data);
  })
}
