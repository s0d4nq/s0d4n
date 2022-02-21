// let ghoul = 1000
// setInterval(()=>{
//     console.log(ghoul);
//     ghoul -= 7
// }, 50)

// const btn = document.querySelector('.btn')
// const clock = document.querySelector('.clock')

// const timerClock = ()=>{
//     let time = 0
//     setInterval(()=>{
//         clock.textContent = time
//         time++
//     }, 1000)
//     btn.removeEventListener('click', timerClock)
// }

// btn.addEventListener('click', timerClock)
// let time = 20
// btn.addEventListener('click', ()=>{
//     setInterval(()=>{
//         if(time >= 0){
//             clock.textContent = time
//             time--
//         }
//     }, 1000)
// })


// const btn = document.querySelector('.btn')
// const popUp = document.querySelector('.pop_up')

// btn.addEventListener('click', ()=>{
//     setTimeout(()=>{
//         popUp.classList.add('show__pop_up')
//         setTimeout(()=>{
//             popUp.classList.remove('show__pop_up')
//         },2000)
//     }, 2000)
// })






// const btn = document.querySelector('.btn')
// const clock = document.querySelector('.clock')


// const showDate = ()=>{
//     setInterval(()=>{
//         let today = new Date()
//     let day = today.getDate()
//     let month = today.getMonth() +1
//     let year = today.getFullYear()
//     let hour = today.getHours()
//     let minutes = today.getMinutes()
//     let sec = today.getSeconds()

//     clock.textContent = `${day}/${month}/${year}  ${hour}/${minutes}/${sec}`
//     },0)
// }

// btn.addEventListener('click', showDate)


// const btn =   document.querySelector('.btn')
// const image = document.querySelector('.image')

// btn.addEventListener('click', ()=>{
//     let num = 1
//     setInterval(()=>{
//         if(num == undefined || num == 3){
//             num = 1
//         }else{
//             num++
//         }
//         image.src = `${num}.png`
//     }, 1000)
// })


const btn = document.querySelector('.btn')

btn.addEventListener('click', ()=>{
    setInterval(()=>{
        const img1 = document.querySelector('.img1')
        const img2 = document.querySelector('.img2')
        const img3 = document.querySelector('.img3')
        let temp = img1.src
        img1.src = img2.src
        img2.src = img3.src
        img3.src = temp
    },1100)
})