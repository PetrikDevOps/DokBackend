# Login (POST)
    Where?
    /login

    format?  
    {name: "name", pw: "cisco :D"}

    res
    {status: Bool, ?user_id:INT, ?errormsg:"String", ?key: "String" }

# Reg (POST)

    Where?
    /reg

    format?
    {name: "name", pw: "cisco :D", email: "email@gmail.com"}

    res
    {status: Bool, ?user_id:INT, ?errormsg:"String", ?key: "String" }

# Hírek (GET)

    Where?
    /news

    res format?
    {post: [{title: "name", disc: "lldalsdlasdas da s das d asdasdasd asdas dasd asdas"}, {title: "name", disc: "dsa dsa das d as das das das as da"}]}

# Naptár

    Where?
    Google naptár implamentáció

    diakonkormanyzat.petrik@gmail.com

# Chat (GET)

    Where?
    /chat

    res format?
    {comment: [{name: "name", msg: "dasda"}, {name: "name", msg: "dads ddas"}]}


# Chat (POST)

    Where?
    /newmsg

    format?
    {user_id: INT, msg: "dasdasd"}

    res
    {status: Bool, errormsg: "String"}

# Live Socket IO server (PORT 2506)

# Tipp (POST)

    Where?
    /sendtipp

    format?
    {user_id: INT, tipp: "dsal"}

    res 
    {status: Bool, ?errormsg:"STRING"}

# Feladat (GET)

    Where?
    /job

    res format?
    {jobs: [{id:INT, job: "name of job", desc: "dsaddsa"}, {id:INT, job: "sec job", desc:"dsany"}]}

# FeladatHelp (POST)

    Where?
    /jobHelp

    format
    {user_id:INT, job_id:INT, msg:"String"}

    res 
    {status: Bool, ?errormsg:"STRING"}

# SzavazásLekérés(GET)

    Where?
    /vote

    res format?
    {votes: [{vote_name: "Vote name", vote_id:INT, list_of_ch: [{op_name: "string", op_id: INT}, op_name: "string", op_id: INT, op_name: "string", op_id: INT]}]} 

# SzavazásLeadás(POST)

    Where?
    /voteTo

    format:
    {user_id: INT, vote_id: INT, op_id: INT}

# GenVote (Post)

    Where?
    /genVote

    format
    {user_id: INT, key: "String", vote_name: "String", list_of_ch:[]}


