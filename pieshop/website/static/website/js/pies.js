window.addEventListener("DOMContentLoaded", function (e) {
    const orderButtons = this.document.querySelectorAll("button[data-order]");

    orderButtons.forEach(function (button) {

        button.addEventListener("click", function (e) {
            const button = e.currentTarget;
            const container = button.parentNode;

            const order = {
                // id: button.getAttribute("data-order"),
                pk: container.querySelector(".pk").getAttribute('value'),
                title: container.querySelector(".title").innerText,
                price: container.querySelector(".price").innerText,
                desc: container.querySelector(".desc").innerText,
                image: container.querySelector("img").src,
            };

            console.log(order);
            
            localStorage.setItem("order", JSON.stringify(order));

            const url = window.location.href.replace("pies/", "order/");
            window.location.href = url; 

        });

    });
});
