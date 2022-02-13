$.getJSON("/templaes/data.json", function(json) {
    console.log(json.jobs); 
    for (index = 0; index < json.jobs.length; index++) {
        // console.log(dataJ);
        display(json.jobs[index]);
    }
});


function display(dataJ) {
    let newCard = document.createElement('div');
    newCard.id = "contain";
    newCard.innerHTML = `
    <div class="product-details">
                    
    <!-- 	Product Name -->
  <h1 align="center">{{det.title}}</h1>
  
  <span class="hint-star star">
    <i class="fa fa-star" aria-hidden="true"></i>
    <i class="fa fa-star" aria-hidden="true"></i>
    <i class="fa fa-star" aria-hidden="true"></i>
    <i class="fa fa-star-half-o" aria-hidden="true"></i>
    <i class="fa fa-star-o" aria-hidden="true"></i>
  </span>
    
  
  <!-- The most important information about the product -->
    <p class="information">{{det.description}}</p>
    
    
  <!-- 		Control -->
  <div class="control">
  
  <!-- Start Button buying -->
  <button class="btn">
  <!-- 		the Price -->
  <span class="price">{{det.pay}}</span>
  <!-- 		shopping cart icon-->
  <span class="shopping-cart"><i class="fa fa-shopping-cart" aria-hidden="true"></i></span>
  <!-- 		Buy Now / ADD to Cart-->
  <span class="buy">Apply</span>
  </button>
  <!-- End Button buying -->
  
  </div>
    
  </div>
  
  <!-- 	End	Product details   -->
  
  
  
  <!-- 	Start product image & Information -->
  
  <!--<div class="product-image">
  
  <img src="${dataJ.img}" alt="Omar Dsoky">-->
  
  <!-- 	product Information-->
  <div class="info">
  <h2>The Description</h2>
  <ul>
    <li><strong>Address: </strong>{{det.city}},{{det.state}},{{det.pin}}</li>
    <!--<li><strong>Min. Skills: </strong>{{det.</li>
    <li><strong>Date: </strong>${dataJ.date}</li>-->
    
  </ul>
  </div>
  </div>
  <!--  End product image  -->
  
  
  </div>
    `;
    const cardArea = document.getElementById("cards");
    cardArea.appendChild(newCard);
    return;
}