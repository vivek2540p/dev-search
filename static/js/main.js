

let searchForm = document.getElementById('fsearch')
let pageLinks = document.getElementsByClassName('page-link')

if (searchForm) {
    for (let i = 0; pageLinks.length > i; i++) {
        pageLinks[i].addEventListener('click', function (e) {
            e.preventDefault()
            let page = this.dataset.page
            searchForm.innerHTML += `<input value=${page} name="page" hidden/>`
            searchForm.submit()
        })
    }
}



let tags = document.getElementsByClassName('project-tag')

for (let i = 0; tags.length > i; i++) {
    tags[i].addEventListener('click', (e) => {
        let tagId = e.target.dataset.tag
        let projectId = e.target.dataset.project



        fetch('http://127.0.0.1:8000/api/remove-tag/', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 'project': projectId, 'tag': tagId })
        })
            .then(response => response.json())
            .then(data => {
                e.target.remove()
            })

    })
}



function toggleChat() {
    const chat = document.getElementById("chatContainer");
    chat.style.display = chat.style.display === "flex" ? "none" : "flex";
  }

  function sendMessage() {
    const input = document.getElementById("userInput");
    const messages = document.getElementById("chatMessages");

    if (input.value.trim() !== "") {
      const userMsg = document.createElement("p");
      userMsg.innerHTML =  input.value;
      userMsg.className = Math.random()<0.5?"bot-message":"human-message"
      messages.appendChild(userMsg);
      input.value = "";
      messages.scrollTop = messages.scrollHeight;
    }
  }
