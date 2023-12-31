form = document.getElementById("form");
input = document.getElementById("input");
select = document.getElementById("search_method");

const sendRequest = async (e, searchText) => {
    e.preventDefault();
    const response = await fetch(`/search?${searchText}&method=${select.options[select.selectedIndex].value}`, {
        method: "POST",
    });
    if (response) {
        location.reload()
        return await response.text()
    }
}

form.addEventListener("submit", (e) => {
    sendRequest(e, input.value)
        .then(r => { console.log(r) });
});
