let inputWidth =  document.querySelector('.width')
let inputHeight = document.querySelector('.height')
let inputColor =  document.querySelector('.color')
let inputRadius = document.querySelector('.brad')
let container =   document.querySelector('.body')
let btnClear =    document.querySelector('.clear')
let btnCreate =   document.querySelector('.create')
let btnUp =       document.querySelector('.up')
let btnDown =     document.querySelector('down')
let btnLeft =     document.querySelector('.left')
let btnRight =    document.querySelector('.right')

let newDiv;
let mTop = 0;
let mLeft = 0;
let iwValue;
let ihValue;
let icValue;
let isRadius;
let isDiv = false;

const createDiv = () =>{
    if(!isDiv){
        iwValue =  inputWidth.value
        ihValue =  inputHeight.value
        icValue =  inputColor.value
        isRadius = inputRadius.value

        if(iwValue >= 50 && ihValue >= 50 && iwValue <= 500 && ihValue <= 500){
            newDiv = document.createElement('div')
            newDiv.style.width =      iwValue + 'px'
            newDiv.style.height =     ihValue + 'px'
            newDiv.style.background = icValue
            
            if (isRadius){
                newDiv.style.borderRadius = iwValue/2 + 'px' 
            }

            container.prepend(newDiv)
            inputHeight.setAttribute('readonly', 1)
            inputWidth.setAttribute('readonly', 1)
            isDiv = true
        }
    }
}

const clearDiv = () =>{
    container.firstChild.remove()
    isDiv = false
    inputHeight.removeAttribute('readonly', 1)
    inputWidth.removeAttribute('readonly', 1)
}

btnCreate.addEventListener('click', createDiv)
btnClear.addEventListener('click', clearDiv)

const blockUp = () =>{
    if(mTop - 10 >= 0){
        mTop -= 10
        newDiv.style.marginTop = mTop + 'px'
    }
}

const blockDown = () =>{
    if(500 - (mTop*1 + ihValue*1 + 10) >= 0){
        mTop += 10
        newDiv.style.marginDown = mTop = 'px'
    }
}

const blockLeft = () =>{
    if(mLeft - 10 >= 0){
        mLeft -= 10
        newDiv.style.marginLeft = mLeft + 'px'
    }
}

const blockRight = () =>{
    if(500 - (mLeft*1 + ihValue*1 + 10) >= 0){
        mLeft += 10
        newDiv.style.marginLeft = mLeft + 'px'
    }
}

btnUp.addEventListener('click', blockUp)
btnDown.addEventListener('click', blockDown)
btnLeft.addEventListener('click', blockLeft)
btnRight.addEventListener('click', blockRight)