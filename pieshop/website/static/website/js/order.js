window.addEventListener("DOMContentLoaded", function(e){

    const order = this.localStorage.getItem("order");
    console.log(order);
    if (order) {
        const pieOrder = JSON.parse(order);    

        const pie = this.document.querySelector(".pie");
        
        const title = pie.querySelector(".title");
        const price = pie.querySelector(".price");
        const desc = pie.querySelector(".desc");
    
        title.innerText += pieOrder.title;
        price.innerText += pieOrder.price;
        desc.innerText += pieOrder.desc; 

        this.document.querySelector("#pie-selector").value = pieOrder.pk;

        const img = pie.querySelector("img");
        img.setAttribute("src", `${pieOrder.image}`);
        img.setAttribute("alt", pieOrder.title);
    }

});