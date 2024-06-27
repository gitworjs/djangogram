function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const handleLikeClick = (buttonId) => {
    const likeButton = document.getElementById(buttonId);
    const likeIcon = likeButton.querySelector("i");

    //서버로 좋아요 api를 호출
    const csrftoken = getCookie('csrftoken');
    const postId = buttonId.split("-").pop();
    const url = "/posts/" + postId + "/post_like"
    
    fetch(url, {
        method: "POST",
        mode: "same-origin",
        headers: {
            // 'Content-type': 'application/json',
            'x-CSRFToken':csrftoken
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.result === "like") {
            likeIcon.classList.replace('fa-heart-o','fa-heart')
        } else {
            likeIcon.classList.replace('fa-heart','fa-heart-o')
        }
    });
}