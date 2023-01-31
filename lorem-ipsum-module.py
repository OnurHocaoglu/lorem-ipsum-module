# Lorem İpsum Module
# 200 Words

def lorem_ipsum(txt=1):

    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam dictum, nisl quis posuere vestibulum, nulla justo dignissim erat, suscipit ullamcorper massa odio in orci. Praesent sed vehicula tortor. Ut facilisis purus quam, pharetra congue mi dignissim quis. Curabitur id odio sit amet ante dictum malesuada sit amet et elit. Morbi sollicitudin, ipsum ac venenatis placerat, ex ex pharetra felis, id congue nisi nulla id velit. Etiam vestibulum tellus at porttitor euismod. Etiam placerat auctor risus, ac sodales lectus porttitor pulvinar. Vivamus ullamcorper sed augue rhoncus dignissim. Phasellus suscipit ornare lectus congue porttitor. Cras euismod pharetra nibh vitae dignissim. Ut nibh enim, commodo non ex vel, sodales imperdiet ligula. Mauris a dui sed metus gravida rutrum. Ut mollis magna sit amet sem pellentesque, vestibulum cursus purus tincidunt. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nam blandit lacus vel pellentesque molestie. Morbi in accumsan neque, sit amet venenatis sapien. Quisque mi elit, convallis sagittis augue nec, suscipit luctus nisi. Duis a est id velit laoreet consequat. Aliquam pellentesque ipsum vehicula ante sodales, sit amet tempus metus mollis. Aenean mollis porttitor faucibus. Morbi et ultrices tellus. Pellentesque quis ligula eu elit consectetur dapibus at non ipsum. Suspendisse."

    lorem = lorem.split(" ")

    lorem = " ".join(lorem[:txt])

    return lorem


print(lorem_ipsum(10))