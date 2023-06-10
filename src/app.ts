import express, { Request, Response } from 'express';

const app = express();
app.use(express.json());

// Login (POST)
app.post('/login', (req: Request, res: Response) => {
    const data = req.body;
    const name = data.name;
    const pw = data.pw;

    // Check username and password
    // ...

    // Send response
    const response = {
        status: true,
        user_id: 123,
        errormsg: '',
        key: 'secret_key',
    };
    res.json(response);
});

// Reg (POST)
app.post('/reg', (req: Request, res: Response) => {
    const data = req.body;
    const name = data.name;
    const pw = data.pw;
    const email = data.email;

    // Register user
    // ...

    // Send response
    const response = {
        status: true,
        user_id: 456,
        errormsg: '',
        key: 'secret_key',
    };
    res.json(response);
});

// Hírek (GET)
app.get('/news', (req: Request, res: Response) => {
    // Get news
    // ...

    // Send response
    const response = {
        post: [
            { title: 'name', disc: 'lldalsdlasdas da s das d asdasdasd asdas dasd asdas' },
            { title: 'name', disc: 'dsa dsa das d as das das das as da' },
        ],
    };
    res.json(response);
});

// Chat (GET)
app.get('/chat', (req: Request, res: Response) => {
    // Get chat messages
    // ...

    // Send response
    const response = {
        comment: [
            { name: 'name', msg: 'dasda' },
            { name: 'name', msg: 'dads ddas' },
        ],
    };
    res.json(response);
});

// Chat (POST)
app.post('/newmsg', (req: Request, res: Response) => {
    const data = req.body;
    const user_id = data.user_id;
    const msg = data.msg;

    // Add new message to the chat
    // ...

    // Send response
    const response = {
        status: true,
        errormsg: '',
    };
    res.json(response);
});

// Live Chat
// Implementation: Live Socket IO server (PORT 2506)

// Tipp (POST)
app.post('/sendtipp', (req: Request, res: Response) => {
    const data = req.body;
    const user_id = data.user_id;
    const tipp = data.tipp;

    // Send tip for processing
    // ...

    // Send response
    const response = {
        status: true,
        errormsg: '',
    };
    res.json(response);
});

// Feladat (GET)
app.get('/job', (req: Request, res: Response) => {
    // Get jobs
    // ...

    // Send response
    const response = {
        jobs: [
            { id: 1, job: 'name of job', desc: 'dsaddsa' },
            { id: 2, job: 'sec job', desc: 'dsany' },
        ],
    };
    res.json(response);
});

// FeladatHelp (POST)
app.post('/jobHelp', (req: Request, res: Response) => {
    const data = req.body;
    const user_id = data.user_id;
    const job_id = data.job_id;
    const msg = data.msg;

    // Send help request for the job
    // ...

    // Send response
    const response = {
        status: true,
        errormsg: '',
    };
    res.json(response);
});

// SzavazásLekérés(GET)
app.get('/vote', (req: Request, res: Response) => {
    // Get votes
    // ...

    // Send response
    const response = {
        votes: [
            {
                vote_name: 'Vote name',
                vote_id: 1,
                list_of_ch: [
                    { op_name: 'string', op_id: 1 },
                    { op_name: 'string', op_id: 2 },
                    { op_name: 'string', op_id: 3 },
                ],
            },
        ],
    };
    res.json(response);
});

// SzavazásLeadás(POST)
app.post('/voteTo', (req: Request, res: Response) => {
    const data = req.body;
    const user_id = data.user_id;
    const vote_id = data.vote_id;
    const op_id = data.op_id;

    // Cast vote
    // ...

    // Send response
    const response = {
        status: true,
        errormsg: '',
    };
    res.json(response);
});

// GenVote (Post)
app.post('/genVote', (req: Request, res: Response) => {
    const data = req.body;
    const user_id = data.user_id;
    const key = data.key;
    const vote_name = data.vote_name;
    const list_of_ch = data.list_of_ch;

    // Generate vote
    // ...

    // Send response
    const response = {
        status: true,
        errormsg: null,
    };
    res.json(response);
});

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});
