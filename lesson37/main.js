const btn = document.querySelector('.btn')
const input = document.querySelector('.input_text')
const list = document.querySelector('.list')
let listArr

if (!localStorage.listArr){
    listArr = []
}else{
    listArr = JSON.parse(localStorage.getItem('listArr'))
}

btn.addEventListener('click', () => {
    let text_value = input.value
    input.value = ''
    listArr.push(text_value)
    console.log(listArr);
    list.innerHTML += createElement(text_value)
    fillList()
    localStorage.setItem('listArr', JSON.stringify(listArr))
})

const fillList = () => {
    list.innerHTML = ''
    if (listArr.length > 0){
        listArr.forEach((item,index) => {
            list.innerHTML += createElement(item, index)
        });
    }
}


const createElement = (text, index) => {
    return `
    <li class="list_item">${text}
    <button onclick="deleteItem(${index})" class="deletebtn btn">Delete</button>
    </li>
    
    `
}

const deleteItem = index => {
    listArr.splice(index, 1)
    fillList()
    localStorage.setItem('listArr', JSON.stringify(listArr))
}

fillList()