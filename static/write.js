let downloadButton = document.querySelector('#download');
let form = document.querySelector('form');
let close = document.querySelector('.close');
let data = '';
form.addEventListener('submit', async function (e){
  e.preventDefault();
  data = form.children[0].value 
  console.log(data)
  if (!data) {
    isError();
  }
  else {
    if (isValid(data))
      downloadButton.style.display = 'block';
    else
      isError();
  }
})
const isError=()=>{
  let error=document.createElement('div')
  error.classList.add('alert', 'alert-danger', 'alert-dismissible', 'fade', 'show')
  error.role = 'alert';
  error.innerHTML = `<strong>Please enter a valid url!!! </strong><button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
  <strong><button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close">
  </button></strong>`
  document.body.prepend(error);
  form.children[0].value = '';
}
const isValid=url=> {
  try {
    url = new URL(url);
  } catch  {
    return false;  
  }
  return url.protocol === "http:" || url.protocol === "https:";
}
downloadButton.addEventListener('click', async function () {
    const options={
        method: "POST",
        body: JSON.stringify({data:data}),
        headers:{'Content-Type':'application/json'}
    };
    let status = '';
    let rep=document.querySelector('.modal-body')
    fetch('/down',options)
      .then(res => {
        console.log('downloading')
        status = res.status;
        return res.blob();
      }).then(blob => {
        if (status != 200) {
          rep.innerText = 'Interrupt Occurred!!!';
          close.style.display = 'block';
          form.children[0].value = '';
        } else {
          download(blob)
          rep.innerText = 'Downloading is finished!!!'
          close.style.display = 'block';
          form.children[0].value = '';
        }
        }).catch(err => {
          rep.innerText = 'Interrupt Occurred!!!';
          close.style.display = 'block';
          form.children[0].value = '';
        });
  downloadButton.style.display = 'none'; 
  close.style.display = 'none';
  rep.innerText = 'Downloading is in progress, Wait for few seconds!!!'
})
