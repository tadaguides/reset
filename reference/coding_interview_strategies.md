# Coding Interview Strategies

## Top Points:
* Be really comfortable with easy questions. This means <5 minutes each, at most. Binary search, sorting, simple data structure operations must be automatic. 
* Medium questions are the most important ones to do in order to prepare for interviews. 
* Don't spend too much time on hard questions: if you are comfortable with mediums, then usually hard questions are just a intricate mix of medium questions. 
* If you can't get to a solution after 30 mins (or 1 hour if you feel like you're close), just look up the solution, and then go back and solve the question in your own code. Don't copy and paste!
* Once you're comfortable solving questions, focus on speed. Mock interviews are good for that, because they give you a time limit and put you under pressure. 
* Target times:
  * Easy: < 5 minutes.
  * Medium: < 15 - 20 minutes.
  * Hard: < 30 - 40 minutes.

---


## Maximizing Your Practice
https://leetcode.com/explore/interview/card/coding-interview-strategy/208/preparation/1354/

* When you start practicing for coding interviews, there’s a lot to cover. You’ll naturally wanna brush up on technical questions. But how you practice those questions will make a big difference in how well you’re prepared.
* Here’re a few tips to make sure you get the most out of your practice sessions.

1. Track your weak spots
  * One of the hardest parts of practicing is knowing what to practice. Tracking what you struggle with helps answer that question.
  * So grab a fresh notebook. After each question, look back and ask yourself, “What did I get wrong about this problem at first?” Take the time to write down one or two things you got stuck on, and what helped you figure them out. Compare these notes to our tips for getting unstuck.
  * After each full practice session, read through your entire running list. Read it at the beginning of each practice session too. This’ll add a nice layer of rigor to your practice, so you’re really internalizing the lessons you’re learning.

2. Use an actual whiteboard
  * Coding on a whiteboard is awkward at first. You have to write out every single character, and you can’t easily insert or delete blocks of code.
  * Use your practice sessions to iron out that awkwardness. Run a few problems on a piece of paper or, if you can, a real whiteboard. A few helpful tips for handwriting code:
  * Start in the top-left corner. You want all the room you can get.
  * Leave blank space between each line of code. This makes it much easier to add things later.
  * Slow down. Take an extra second to think of descriptive variable names. You might be tempted to move faster by using short variable names, but that actually ends up costing more time. It’ll make your code harder to debug!

3. Set a timer
  * Get a feel for the time pressure of an actual interview. You should be able to finish a problem in 30–45 minutes, including debugging your code at the end.
  * If you’re just starting out and the timer adds too much stress, put this technique on the shelf. Add it in later as you start to get more comfortable with solving problems.

4. Think out loud
  * Like writing code on a whiteboard, this is an acquired skill. It feels awkward at first. But your interviewer will expect you to think out loud during the interview, so you gotta power through that awkwardness.
  * A good trick to get used to talking out loud: Grab a buddy. Another engineer would be great, but you can also do this with a non-technical friend.
  * Have your buddy sit in while you talk through a problem. Better yet—try loading up one of our questions on an iPad and giving that to your buddy to use as a script!

5. Set aside a specific time of day to practice.
  * Give yourself an hour each day to practice. Commit to practicing around the same time, like after you eat dinner. This helps you form a stickier habit of practicing.
  * Prefer small, daily doses of practice to doing big cram sessions every once in a while. Distributing your practice sessions helps you learn more with less time and effort in the long run.


## REPEATO Method to Ace Coding Interviews
https://www.fullstackacademy.com/blog/whiteboard-coding-interviews-a-6-step-process-to-solve-any-problem
* R(epeat): Repeat the question
* E(xamples): Write out examples
* A(ppraoches): Describe your approaches
* C(ode): Write your code
* T(est): Test your code
* O(ptimization): Optimization


## On: Acing the Coding Interview, by Nick Ciubotariu (ex. Microsoft/Amazon, current CTO @ Venmo)
https://medium.com/@nick.ciubotariu/ace-the-coding-interview-every-time-d169ce1fd3fc
### STAR structure for interview answers (situation/task/action/result)
### Interview Strategies
  * KP: Practice with pen/paper or whiteboard
  1. write down interview question in your own words
  2. break down problem into smaller parts => create approach to solve problem
  3. write pseudo-code => write real code
  4. walk through code: look for bugs
  5. test your code: pay attention to null checks/corner cases
  * KP: Take time to really understand the problem before moving on.
  * Doing this, you will LEARN & INTERNALIZE the subject matter.
  * KP: Run solution in IDE ONLY when you have given it your best shot and exhausted the solution on paper.
  * Write the question on paper => you can review it later.
### Key Topics:
  1. Trees (esp. Binary Search Trees)
  2. Big O Notation (time/space complexity)
  3. HashTables
  4. OO Design/Systems Design
  5. Algorithms: BFS/DFS, Binary Search, Merge Sort
  6. Arrays
  7. Recursion
  8. Linked Lists
  9. Stacks/Queues
  10. Bit Manipulation
### Interview Prep Philosophy: "Eat the elephant one bite at a time"
  * Why? CS is dense and hard to digest
  * Solution:
    * Pick an area, increase difficulty as you go, try solving 2-3 problems per day
    * Dedicate one day to review the week's questions/study topics (CRUCIAL FOR KNOWLEDGE RETENTION)
* Misc Tips:
  * Treat interviews like meeting new people with some fun challenges thrown in.
  * If you have a bad interview, shake it off immediately #NextPlay
* Leading up to interview day
  * One week before:
    * review study material
    * research company/position
    * polish soft skills/resume highlights
  * The night before:
    * KP/TOP RULE: GET GREAT SLEEP!!!!!
  * Day of interview:
    * Be on time!
    * Relax and listen closely!
    * When given a question, ask clarifying question (do not start coding right away!)
    * KP: Always solve the problem algorithmically first
      * Talk through approach with interviewer
      * Draw out small sample dataset
      * Write pseudocode in steps, explaining each step
      * Write real code, talk through code
      * Test code against dataset you created ("run code")
      * KP: Write test cases and run tests
      * KP: Write clean and compilable code
      * KP: Relax and show confidence!!!


## LeetCode Grinding Guide
* https://www.reddit.com/r/cscareerquestions/comments/6luszf/a_leetcode_grinding_guide/
* First of all, if you think studying CS fundamentals alone can land you offers, you may stop reading here. This guide is intended for those who would like to equip themselves with the necessary skills through LeetCode to tackle technical interviews. Grinding LeetCode is more than just memorizing answers, you have to learn the problem-solving patterns by heart and apply them to similar problems. The number of problems you have solved in LeetCode is only one of the indicators of your familiarness to the patterns, learning the patterns is more than only numbers.

### Checkpoint 0: Beyond the CS Fundamentals
* This guide assumes that you have at least heard of the basic tricks such as two-pointers and bit manipulation from CTCI or similar books. You do not have to master them, knowing what they are can help you study the solutions from LeetCode better. If you have studied only the CS fundamentals, you may want to have a quick look at the books before starting LeetCode.

#### Easy Problems
* Easy problems are intended to help you get familiar with the basic tricks. Usually, they have trivial brute force solutions. What you need to learn is to apply the tricks to improve your brute force solutions.
* Checkpoint 1: Practicing the Basic Tricks: If you randomly open a few easy problems of each data structure or algorithm and you can pinpoint the optimal solutions and implement them in a few minutes, you may move on to the next checkpoint.
* Study Guide
  * Sort the problems by acceptance rate descending. Problems with higher acceptance rates are relatively easier among the pool of easy problems.
  * Try to solve the problems with no hints at least with brute force solutions.
  * It is tempting, but not helpful, to abuse the "run" button. Try Easy ones with a goal to get accepted on the first submission, since this more realistically models a whiteboard situation. It forces you to think of all the use cases yourself. Thanks /u/dylan_kun for the tip.
  * Study how the top solutions apply the tricks to improve the performance. Sometimes solutions are up-voted just because they are short and they may not be well documented. Read also the comments below and do not feel shame to ask for clarifications.
* Once you are comfortable with the basic problem-solving patterns, go back to checkpoint 1 and decide if you would like to move on.

#### Medium Problems
* Medium problems are intended to train your skills in seeing through the problems. They are usually disguises or variations of easy problems. Brute force solutions sometimes may lead to time limit exceeded (TLE). What you need to learn is identifying what solving patterns the problems are asking for.
* Checkpoint 2: Problem Pattern Recognition: If you randomly open a few medium problems of each data structure or algorithm and you can identify what problems they are disguising at and can implement close-to-optimal solutions within half hour, you are ready to challenge the hard problems.
* Study Guide
  * Carefully read each word of the problem statements and look for hints about solving patterns. For example, the number of ways for a task indicates DP, string transformation with dictionary indicates BFS / DFS / Trie, looking for duplicate or unique elements indicates hashing or bit manipulation, parsing indicates the use of stack. If you need a compiled list of tricks and indicators of when to use what, you may check out the book Competitive Programmer’s Handbook.
  * When you have a rough idea about the direction, you are half way to go. Try to at least implement a suboptimal solution. It is okay that yours is not optimal, people spent much effort to polish their solutions to optimize them.
  * Once you have a suboptimal solution, you may head over to the top solutions to learn what you can improve and any alternative methods to solve the same problem.
  * Try to thoroughly understand the thought process and implement the optimal solutions based on your understanding without looking at any hints.
* Once you are comfortable with seeing through the problem patterns, it is time for the grand challenges.

#### Hard Problems
* Hard problems are bar-raisers. They are intended to be hard and make you struggle. Usually, 45 minutes are barely enough for you to come up with a working solution. What you need to learn is identifying the right directions to solve the problems more than just brute force.
* Checkpoint 3: Graduation Check: Hard problems usually have constraints that make the typical tricks not applicable. If you are comfortable with improving existing tricks to solve those problems more than brute force, you are good to go. The time limit is not that important here, you need to learn how to bridge the gap between typical tricks and those constraints.
* Study Guide
  * Solving the problem is more important than finding the optimal solution. Your first task is to at least come up with a brute force solution. Dropping the time and/or space constraints usually help you identify one.
  * Identify what parts of your solution can be optimized to satisfy those constraints. This has been covered by many books and articles such as the BUD approach from CTCI so I would not go into details.
  * If you struggle to improve your solution, time to head to the top solutions. Understanding the thought process is critical here. You need to learn what are the right data structure and algorithms to use and how those solutions handle the corner cases.
* Once you are comfortable with the stress from the hard problems, try to solve other hard problems with suboptimal solutions.

---

## LeetCode Strategy: 
* https://www.youtube.com/watch?v=GbyXxUDVeAo
* Top LC Questions: https://www.teamblind.com/post/New-Year-Gift---Curated-List-of-Top-100-LeetCode-Questions-to-Save-Your-Time-OaM1orEU
* https://www.teamblind.com/post/My-Leetcode-strategy-t6EU8L45

* Fundamentals: I have a pretty good knowledge of fundamentals. If you don't, I 100% recommend you go through an algorithms book. Yes, I know, it's no fun if you haven't done a class on it before, but I believe is the best way to at least get a grasp of everything. I dislike interview preparation books (CTCI is just bad in my opinion), but I guess they're better than nothing. I suggest CLRS as a first algorithms book. You don't need to understand the math behind it, but at least be comfortable in how to design an algorithm.

* Leetcode: I first did the "Top Interview Questions" collection (available for free), I did the medium collection fully and some of the problems from the hard collection. It's good because it exposes you to a lot of different areas (you need to be good at ALL of those).

* Then I bought Leetcode Premium. This unlocks company tags (useless for some companies like Google, more useful for Microsoft and others). I spent 90% of my time doing the "mock interviews". Trust me, that was the thing that really made me excel in my interviews. The mock interviews give you a strict time limit, and in the end, they give you a percentage rating against all the other people that did the same mock interview set. This is much, much more useful than looking at the percentile for individual problems since many people just copy and paste the code from the top most-voted answer and get 100% percentile, making the average score go up. In a mock interview you don't have access to the discussion forum (of course, you can open another tab and cheat, but I feel like most people won't do that).

* Be really comfortable with easy questions. This means <5 minutes each, at most. Binary search, sorting, simple data structure operations must be automatic. Medium questions are the most important ones to do in order to prepare for interviews. Don't spend too much time on hard questions: if you are comfortable with mediums, then usually hard questions are just a intricate mix of medium questions. If you can't get to a solution after 30 mins (or 1 hour if you feel like you're close), just look up the solution, and then go back and solve the question in your own code. Don't copy and paste!

* Once you're comfortable solving questions, focus on speed. Mock interviews are good for that, because they give you a time limit and put you under pressure. * My target times were:
  * Easy: < 5 minutes.
  * Medium: < 15 - 20 minutes.
  * Hard: < 30 - 40 minutes.

* I achieved the desired target time for easy and medium questions, but hard questions can be really frustrating and never achieved a consistent < 40 minutes. Some hard questions I was never able to solve, and that's fine. Focus on medium.

* My ratio was 20/70/10 easy/medium/hard. I had one month to prepare, I did around 200 leetcode I would say (unfortunately problems solved in mock interviews are not counted towards the total solved, so I'll never know how many I've actually solved).

* Then, identify one area where you suck. In my case, dynamic programming. Read up tutorials / book chapters / explanations on that area, and understand the solution to common problems really well (like rod cutting for dynamic programming). Then go to the relative section on Leetcode and start doing them until you feel good. After doing like 15 dynamic programming questions I finally felt like I could get the hang of it.

* In terms of tutorials: do not use random online resources! I can't stress this enough. There's so much crap online that you don't want to get inspiration from! GeeksForGeeks is a terrible resource, for example. Answers are often wrong, with bad English, terrible explanations, and the site has a horrible interface. Prefer blog posts from reputable sources (like actual interviewers), or books. Just search your problem on Google and choose wisely (look at multiple explanations!).

* TL;DR: Leetcode mock interviews saved my life. Use real resources, not random online blogs. Focus on correctness, and then speed.

## Best habits for coding interview prep
https://www.teamblind.com/post/Habits-when-preparing-for-interview-Fa1i7Mz6
* "You are looking for tricks when the only trick is to be good or practice until you are."
* "I was always afraid of failing interviews so I'd put off any company I really wanted to join until I was "ready". Guess what? You're never ready. I recently started interviewing aggressively a month ago and have 2 offers today. Throw enough stones at a wall, and something will stick."
* "Those people who cleared Google by practicing less than 10 problems just lucked out. My advice is fail fast. Practise for couple of weeks, schedule interview with non FANG and see how you perform. Don't spend way too much time preparing. Trust me, even if you prepare for 2 years, there is still no guarantee that you will do well on the interview day."
* "Interview until it feels like a practiced speech."
* "Those who cleared it in under 10 question have always been practising on other platforms or had a competitive programming past. My only habit before I cleared Google L3 was to do leetcode daily. Barring one day I did leetcode daily since 3rd Sep to end of November. I had done ~400 questions when I gave my onsite and I got the offer."
* "I’ll share my personal from the last job change (Amazon):
1. Sleep routine - did change 6 hours a night unfortunately with kids plus 1 8-9 hours night a week
2. Exercise whenever I get to
3. Routine - on weekdays 1.5 to 2 hours of leetcode in the evening and double that on weekends
4. Start with ctci to make sure you cover the basics , theory and common patterns and only then move to leetcode
Space interviews to 1-2 a week tops so you can leetcode premium per company / do research on what each company and tune your prep towards each one
Do couple of non faang before faang to realize where you are and remove the nervousness
I prepped for about 1 month before starting to submit resumes and got to onsites at the 1.5-2 months line which was perfect for me. My attention span and patience for leetcode at that amount was starting to end. Interviewed at 5 places - 3 of them faang. Got yes from 3, no from one and process was too slow at the last one due to headcount at the location I wanted. Only submitted to places I would really work for - 5 out of 5 returned my calls - most of them within a couple of days. All internal referrals of sorts. I had about 1-2 interviews a week so in total it was 3 weeks - I notified the first two companies that it would take me couple of weeks to get decision made. And the last two that I have offers in hand. If you’re clear with the recruiter about the timeline and open - they can usually work it out. Had unlimited pto and free work from home policy. So I was sick one day, off with the kids another , visiting my brother on family matters and one interview I managed to do after my regular work hour. In total I took days off only for onsites and worked from home for the rest of the interviews / scheduled them after work time."
* "What worked for me was to do as many real interviews. Did about 1 coding problem a day for about 2 months. Failed first few phone screens, then passed next dozen. No offers on first several onsites. Ended up with 2 offers after a dozen attempts. I go through this every few years but have been improving. I’d consider myself a late bloomer."
* "Numbers of questions is less important than covering most categories. Also prepared for system design, but didn’t practice mocks(this was a mistake in hindsight). I was spending less hours at work, but felt more productive after doing coding on leetcode ( this is one thing that surprised me, preparing for interviews does help learn things which you normally won’t go out and teach yourself)
Q: Anything else that you think were consciously helpful??
A: I failed few interviews, some at phone screen level. This is expected, dont overthink if uou get rejected, but get a sense of how you can do better. Do mock interviews(specially system design), interviewing is another skill that you get better as you do more. If you feel unprepared postpone the interviews."
* "I know a lot of people who have cracked FANG and other tier 1 companies. Most of them used to practice ~2 hours in the morning before work and in the evening post work. This also had other positive effects on them like waking up early, keeping mind active (since office work becomes menial at times) and most importantly (maybe completely unrelated) made them efficient at office. They knew they couldn't afford to waste time in office nonsense."
* "Create an interview "ladder" in order of increasing difficulty and preference( how much you want to work there). Lower preference, easy interviews on the bottom and higher preference, harder ones on top. Start prepping, and talk to the companies lower down. They act as tests for your interview prep strategy. Identify and fix gaps in your preparation. Repeat for every level up in your interview ladder. For prep, spend half an hour every day initially on easy problems, then build up to an hour on medium and hard, Just like training for a marathon. Keeping it fun and interesting is very important. Have cheat days when you skip leet and do something fun instead. Keeps the motivation up. Overhauling your schedule like you are suggesting may sound great to start with, but it probably isn't sustainable."
* "Preparation makes me confident so I always have to be over-prepared. I basically read through the job description and bullet point every skill, term, topic mentioned in the post. Then I went through the bullet points again and added more for any additional adjacent skills that would be required. I made sure I could provide 3 types of talking points for each bullet."
  * provide the 5 Ws (who/what/when/where/why)
  * provide an example
  * provide an example of my experience with this topic


## Getting that job at Google
http://steve-yegge.blogspot.com/2008/03/get-that-job-at-google.html
* Warm-up #1: Study an algorithm book
  * This helps with problem identification: recognize certain problems are best solved with certain data structures & algorithms
  * Suggested: Algorithm Design Manual (Skiena), Intro to Algorithms (CLRS)
* Warm-up #2: Do mock interviews!
### Tech Prep Tips:
* Algorithm Complexity: you need to know Big-O. It's a must. If you struggle with basic big-O complexity analysis, then you are almost guaranteed not to get hired. It's, like, one chapter in the beginning of one theory of computation book, so just go read it. You can do it.
* Sorting: know how to sort. Don't do bubble-sort. You should know the details of at least one n*log(n) sorting algorithm, preferably two (say, quicksort and merge sort). Merge sort can be highly useful in situations where quicksort is impractical.
* Hashtables: hashtables are arguably the single most important data structure known to mankind. You absolutely have to know how they work. Again, it's like one chapter in one data structures book, so just go read about them. You should be able to implement one using only arrays in your favorite language, in about the space of one interview.
* Trees: you should know about trees. I'm tellin' ya: this is basic stuff, and it's embarrassing to bring it up, but some of you out there don't know basic tree construction, traversal and manipulation algorithms. 
  * You should be familiar with binary trees, n-ary trees, and trie-trees at the very very least. 
  * Trees are probably the best source of practice problems for your long-term warmup exercises. 
  * You should be familiar with at least one flavor of balanced binary tree, whether it's a red/black tree, a splay tree or an AVL tree. You should actually know how it's implemented. 
  * You should know about tree traversal algorithms: BFS and DFS, and know the difference between inorder, postorder and preorder. 
  * You might not use trees much day-to-day, but if so, it's because you're avoiding tree problems. You won't need to do that anymore once you know how they work. Study up!
* Graphs: Graphs are, like, really really important. More than you think. Even if you already think they're important, it's probably more than you think.
  * There are three basic ways to represent a graph in memory (objects and pointers, matrix, and adjacency list), and you should familiarize yourself with each representation and its pros and cons.
  * You should know the basic graph traversal algorithms: breadth-first search and depth-first search. You should know their computational complexity, their tradeoffs, and how to implement them in real code.
  * You should try to study up on fancier algorithms, such as Dijkstra and A*, if you get a chance. They're really great for just about anything, from game programming to distributed computing to you name it. You should know them.
  * Whenever someone gives you a problem, think graphs. They are the most fundamental and flexible way of representing any kind of a relationship, so it's about a 50-50 shot that any interesting design problem has a graph involved in it. Make absolutely sure you can't think of a way to solve it using graphs before moving on to other solution types. This tip is important!
* Other data structures
  * You should study up on as many other data structures and algorithms as you can fit in that big noggin of yours. You should especially know about the most famous classes of NP-complete problems, such as traveling salesman and the knapsack problem, and be able to recognize them when an interviewer asks you them in disguise.
  * You should find out what NP-complete means.
  * Basically, hit that data structures book hard, and try to retain as much of it as you can, and you can't go wrong.
* Math
  * Some interviewers ask basic discrete math questions. This is more prevalent at Google than at other places I've been, and I consider it a Good Thing, even though I'm not particularly good at discrete math. We're surrounded by counting problems, probability problems, and other Discrete Math 101 situations, and those innumerate among us blithely hack around them without knowing what we're doing.
  * Don't get mad if the interviewer asks math questions. Do your best. Your best will be a heck of a lot better if you spend some time before the interview refreshing your memory on (or teaching yourself) the essentials of combinatorics and probability. You should be familiar with n-choose-k problems and their ilk – the more the better.
  * I know, I know, you're short on time. But this tip can really help make the difference between a "we're not sure" and a "let's hire her". And it's actually not all that bad – discrete math doesn't use much of the high-school math you studied and forgot. It starts back with elementary-school math and builds up from there, so you can probably pick up what you need for interviews in a couple of days of intense study.
* Operating Systems
  * This is just a plug, from me, for you to know about processes, threads and concurrency issues. A lot of interviewers ask about that stuff, and it's pretty fundamental, so you should know it. 
  * Know about locks and mutexes and semaphores and monitors and how they work. Know about deadlock and livelock and how to avoid them. 
  * Know what resources a processes needs, and a thread needs, and how context switching works, and how it's initiated by the operating system and underlying hardware. 
  * Know a little about scheduling. The world is rapidly moving towards multi-core, and you'll be a dinosaur in a real hurry if you don't understand the fundamentals of "modern" (which is to say, "kinda broken") concurrency constructs.
  * The best, most practical book I've ever personally read on the subject is Doug Lea's Concurrent Programming in Java. It got me the most bang per page. There are obviously lots of other books on concurrency. I'd avoid the academic ones and focus on the practical stuff, since it's most likely to get asked in interviews.
* Coding: You should know at least one programming language really well, and it should preferably be C++ or Java. C# is OK too, since it's pretty similar to Java. You will be expected to write some code in at least some of your interviews. You will be expected to know a fair amount of detail about your favorite programming language.


## Getting that job at Facebook
https://www.facebook.com/notes/facebook-engineering/get-that-job-at-facebook/10150964382448920


## Comprehensive Data Structure and Algorithm Study Guide
https://leetcode.com/discuss/general-discussion/494279/comprehensive-data-structure-and-algorithm-study-guide


## From 0 to Success with LeetCode
https://leetcode.com/discuss/career/216554/From-0-to-clearing-UberAppleAmazonLinkedIn
* Don't be demotivated at your current level. I started from a place where I was bombing every interview and now I've done much better than what I was expecting. Start and be consistent.
* Try getting comfortable in every topic. Don't leave anything behind.
* Don't spend more than an hour on any question. If you can't figure out the solution, mark it and revisit later.
* Use the discuss forums. They are literally the best part about Leetcode and a key differentiator why no other platform can match up to Leetcode in terms of interview prep.
* Upsolve when you can't solve a problem - i.e look at the solution, understand and then do it again on your own.
* Keep taking notes about what a problem is teaching you. Keep revisiting them. Spaced repitition helps in committing things to memory.
* Don't be in a hurry. Enjoy the ride :)
* The reason I was hooked to Leetcode was the no-bullshit question format, with a clean and intuitive UI. I decided to do two questions a day consistently, gauge my progress over time and then schedule my interviews. When I first started out, I found even the ‘Easy’ questions hard to pass in the first attempt. I was easily spending 45 minutes on trivial questions. As time progressed, I started seeing improvements. In about two weeks, I was solving ‘Easy’ questions in 20-25 minutes and most of them were passing in my first attempt.
* I decided to proceed to Medium questions and the same story repeated. Found them extremely hard, but as time progressed, I could solve a good number of those questions as well. I have to admit that I can do very few hard questions within an hour even after solving 250+ questions. And sometimes it takes hours to understand the solution as well.
* Eventually I tried taking out Leetcode premium. I took it for a month first, and loved it, so I took a yearly subscription. The best part about premium subscription is that you get questions sorted company wise and frequency wise. I would prepare by targeting the company specific questions for the big players (Amazon, Apple, LinkedIn, Facebook, Microsoft, Uber, Google etc.) and then by frequency. It worked out great for me, and it is especially useful when you are running under a time crunch.


## There are no shortcuts
https://leetcode.com/discuss/interview-experience/505108/nda-google-l4l5-japan-feb-2020-pending-offer

* Status: BS, 5+ Yoe in Tier-1 Company (In Japan), Top University in Japan
* Position: L4/L5
* Location: Japan
* Date: Feb 2020

I just want to start by saying big thanks to Leetcode and the community here. I felt it is a much more fair game now, since everyone can access the same amount of resources.
Background
* I was contacted every year by Google recruiter for several years, but I loved my job and refused every single time. Until late last year, I think I needed a change and proactively contact the recruiter who approached me before. I told her I am ready to apply but need some time to prepare. She told me to prepare first and then let her know 1 month before I was ready for phone interview.
Preparation
* I started my preparation around October. I used Leetcode for practicing, Geeks4Geeks for refreshing, CLRS+Algorithms (Sedgewick) for references, educative.io for System Design. I really love math and algorithms, so it was really enjoyable.
Technical Phone Screen
* After 1,2 months (December), I got my phone interview scheduled on January. I still have another month to prepare, but I feel pretty confident at this point.
The interviewer went straight to ask a programming question. One was related to tree traversal (similar to LC Medium), which I solved in 10 minutes (concise+fast). He then moved on to ask an LC Hard level problem. I have never seen it before, but I figure out I need to use Line Sweep, so I coded and made it work. I missed on edge case, but I noticed it myself and was able to partilly resolve that.
8AM the next morning, I received an email from my recruiter to schedule a phone call from 9AM, and the wording really sounded like bad news. I searched on Blind "Google phone interview call the next day" or something like that. More than half said it was bad news, and I was really confused, since I thought I did OK. Thankfully, the recruiter just tried to talk to me to make sure my experience matched the feedback, which was positive.
Onsites
* 3 coding interviews + 1 System Design + 1 Googliness
* 1st, I was asked to code in Laptop so the interviewer didn't need to note my code :). I didn't know I would have other choice other than the whiteboard, but I was happy to accept. He started with a very basic question, then follow up, then another follow up (anyone knows graph would be able to crush these questions easily). He then asked me another question, kind of strange question, I think I was able to analyze and made a working solution (probably not optimal), but I think he was happy with it since it was only 10 minutes left.
* 2nd interview was Googliness, so you know, a bunch of behaviors.
* 3rd interview is another coding, he started by asking an LC-Easy question, I made it work in 10 minutes including testing time, so he moved on to ask an LC-Medium question. I explained the logic, how I would do it, he clearly knew that I was in the right track, so he told me no need to code, and keep asking follow up questions (generic, thread safe, etc).
* 4th interview, so far, the only one I felt challenged. It was a very interesting question, which I never seen before (not similar to any LC I know). After analyzing it, I was able to come up with the solution by using Graph (It's Google, prepare for GRAPH) representation and cycle detection. I barely finished coding before time, and we tested it together, and the interviewer told me it was correct (so nice of him, some interviewers won't tell you if you're wrong or correct).
* 5th interview was System Design, I was worried about this as I don't really know what to expect. However, I was so lucky, he asked me a question that I knew so well that after 15 minutes asking, he litterlly told me that he would give up asking this question (since he realized that I knew too much) and switch to another one. The next question, is again, something I built before, so I was able to come up with a workable design and answer all follow up questions.
Results
* I was called by my recruiter 2 hours after my interview and she told me the initial feedback was very positive, with zero red flag. I am still awaiting hiring commitee decision now. As for level, the recruiter told me it will be either L4 or L5. Finger crossed.

Others

* Take a long vacation! I used 35 days off (with good excuse, and not continuous) + Winter vacation.
* Buy a big WHITEBOARD at home!!! That's the first thing I did in October.
* I did a crazy amount of LC, 613 Mediums, 213 Hards. I would say 70% medium and 50% of hard I could do by myself, the rest I need to read the solution or hints or discussion. I know lots of people do a lot less, but I just wanted to make sure I prepared the best that I can. I learned a lot, probably too much. Some of my favorite topics are: Segmented Tree, Line Sweep, Cycle Detection, Sliding Window.
* Try mock interview. It helped me prepare mentally for actual interview. I felt the time constraint, always push myself. My overall score in October was 5.5, and now, it is 9.4. 2 weeks before the onsite at Google, I did 10 Google onsites, average time to complete is about 40 minutes. The high score is kind of cheating, since at the time I started to do mock again, I already finished "a lot" of hard + medium problems. Still, I felt I made some progress.
* Try to code fast and concise. It will make it a lot easier to impress in an interview, since the faster you code, the more time you can think.
* Try to really really understand a solution. Try to classify what techniques should be used in what problems. I think this is the skill that will make you thrive in an interview. At the end, you will most likely meet a problem you never met before.
* Always read the solution even if you can do the problem yourself. You can find something new!
I already have a competing offer in hand, so the process from onsites for me is very fast. I'd recommend everyone has a competing offer before doing interview with FAANG, even it actually cannot compete financially, it may help to speed up the process.
* Big thanks again and good luck to everyone!


https://leetcode.com/discuss/interview-experience/521537/Google-or-L4-or-MTV-or-Feb-2020-Offer
* Make sure what level you are interviewing for. There is no system design for L3 and L4. My recruiter told me I may be qualified for L5 so he sent me system design prep material. I studied system design very hard. However they downgraded me to L4 "before" my onsite and didn't let me know. I found that out on the onsite day. Obviously coding questions at onsite were easier than phone screens.
* Google allows one failure and considers it as an outlier. They also evaluate how the interviewers performed interviews in the past. I have seen other people completely bombed one round but still received an offer. So, if you think you didn't do well on one round, keep trying hard on the rest of the interviews. This is onsite only. If you fail phone screen, it's over.
* Have Google onsite first if you are applying multiple companies. (Google takes longer than any other company. If you have onsite at other companies first, you can't have all the offers on the table at the same time.)
* For coding, leetcode (easy 79, medium 133, hard 43. Total 255) and Grokking Dynamic Programming Patterns for Coding Interviews course (https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews). I had difficulty understanding how to solve DP questions. This course helped me a lot. 
* Then did mock interviews on interviewing.io A LOT. It's a free service.
* For system design, grokking system design course, Designing Data-Intensive Application book, lots of youtube videos. I spent 6 months in total.
* I solved 255 questions. easy 79, medium 133, hard 43. (I solved only high-frequency problems for easy and hard level.)
* Q: Congrats! What was your prep strategy? how did you leetcode, why did you decide to practiced toplogical sort a lot?
  * A: Not only topological sort lol I practiced writing Dijkstra, Bellman-Ford, Quick Select, Union Find, KMP, Rectangle Area in Histgram etc within 10 min without a bug. Many times.



https://leetcode.com/discuss/interview-experience/505412/google-mtv-l4-offer
* Just wanted to share my interview experience:

I applied to google in December and had my onsite in the same month, because of the NDA I can't disclose specific problems.

The entire preparation process for me took 7+ months, during this time I experienced rejections from Pinterest, Amazon and Dropbox but I used these rejections as an inspiration to keep pushing myself to improve, I also had offers from other companies which I declined since.

My interview strategy was the following:

* My strategy for problem solving is: spend 20-25 minutes trying to figure out which pattern to use for each problem, go through each topic and make sure I get enough experience with every pattern. If I can't solve during 25 minutes then just look at the solution and if this is not helpful, try to look for external resources - there are some amazing youtube channels.
* Completely read and go through each problem in "Cracking the coding interview"
* Study every day for 4+ hours, every study session was focusing on a algorithmic subject or so
* Being able to solve problems under a 20-25 minute mark for every major algorithmic category labeled under leetcode, leaving DP programming as a last subject of study. Every time I start working on a subject I would start with the easy problems and if I couldn't solve it I would look at the solution, I think timing how long it takes you to produce a solution is important since during interviews (in many companies) you might be asked to talk about a project and then jump into problem solving, shorting the 45 minute mark you typically have
* Being able to communicate efficiently my ideas during the onsite
* During the onsite I would even recommend solving the problem or at least mentioning a solution you thought of even if it's not optimal
Took me a lot of rejections but I finally did it and I would say leetcode is definitely a tool that can help you.


https://leetcode.com/discuss/interview-experience/424540/Google-or-L5-or-MTV-or-Oct-2019-Offer
* Status: Software Engineer with 15 years of Professional Experience
* Position: Google L5
* Location: Mountain View, CA
* Date: October 14, 2019

Background:

Hi, my name is Clayton. First off I'd like to give a big thanks to the folks at leetcode (both problem setters and problem solvers), the questions and solutions posted on this site are helpful for understanding algorithms from multiple perspectives expressed via different thought processes and languages. I've paid for two 1-year leetcode subscriptions so far, and I strongly feel those were the two best investments I've made in years. I've been a professional software engineer since I graduated with a B.S. in Computer Science in 2004 from the University of Arizona. I honestly never really learned much about algorithms in my undergraduate studies. I simply learned enough about them to pass some tests. During my career, I slowly forgot whatever I did learn about algorithms. The majority of my professional work was performed in the wireless industry where I developed a highly proprietary skillset. When it was time for me to move on to the next chapter of my career, I had a very hard time with interviews. I was extremely uptight, nervous, and anxious about interviewing; and I failed 100% of the technical phone screens I attempted. I thought to myself, "What's wrong with me? Why am I receiving so many NOs?" Then I took a leetcode contest for the first time and answered none of the questions during that contest. This was a shock for me: as if this objective measurement of sub-optimal performance slapped me straight in the face. So I decided to start learning again, basically from scratch. This was an extremely slow and frustrating experience at first. I would regularly take 1 or 2 weeks to solve easy leetcode problems. However, I stuck with it and found help in the solutions posted in discussion boards associated with each problem.

==> Preparation:
* I started using leetcode to study algorithms and data structures about 2 years ago in 2017 after I totally bombed a handful of technical phone screens. I consistently set aside 30-60 minutes each day to solve leetcode problems.
* I also believe the following 3 online courses were extremely beneficial to help my mind "shift gears" to understand the fundamental basics of algorithms and data structures:

  * Learning How to Learn: Powerful mental tools to help you master tough subjects
  * Tim Roughgarden's Algorithms Specialization
  * UCSD's Data Structures and Algorithms Specialization

==> Contests:
* On average I currently solve 1 or 2 questions during each Leetcode contest. You can check out my Leetcode profile here: https://leetcode.com/claytonjwong/. I'm definitely not the sharpest tool in the shed, but I am willing and able to learn (...and keep learning ...and never give up!).
* Only once did I answer all 4 questions correctly during contest 127
1005. Maximize Sum Of Array After K Negations
1006. Clumsy Factorial
1007. Minimum Domino Rotations For Equal Row
1008. Construct Binary Search Tree from Preorder Traversal
* I solved 2 questions during the most recent virtual contest 162. And I solved the 3rd question about 5 minutes after this virtual contest ended:
1252. Cells with Odd Values in a Matrix
1253. Reconstruct a 2-Row Binary Matrix
1254. Number of Closed Islands
* I've only solved a handful of "hard" questions. Each contest's 4th question is usually the "Hard" question, and I usually do not get to the 4th question before the contest ends. I hope it's reassuring and helpful to know that having the ability to consistently solve a couple easy/medium questions is considered "good enough". I suggest focusing on the fundamentals, not the outliers. I estimate solving 45% easy, 45% medium, and 10% hard. Honestly 10% is probably a high estimate for solving "hard" questions, but the point I'm trying to make is the majority of my time is currently consumed by solving easy and medium questions.

==> Phone Interviews: I had two technical phone interviews, each about 1 hour to answer 1 question. I believe I had a second technical phone interview because I barely "passed" the first technical phone interview.

* Round 1: The first phone interview question was solved by a greedy algorithm similiar to the following leetcode questions:
455. Assign Cookies
759. Employee Free Time
860. Lemonade Change
1103. Distribute Candies to People

* Round 2: The second phone interview question was solved by a linear scan and processing of input in a well-defined manner similiar to the following leetcode questions:
739. Daily Temperatures
1109. Corporate Flight Bookings
1186. Maximum Subarray Sum with One Deletion
1191. K-Concatenation Maximum Sum
1218. Longest Arithmetic Subsequence of Given Difference


==> Onsite Interviews: I had 4 technical interviews, 1 lunch break "interview", and 1 behavioral interview. The first 3 technical interview questions were similiar to the following 3 categories of Leetcode questions:

* Round 1: Parenthesis
20. Valid Parentheses
678. Valid Parenthesis String
856. Score of Parentheses
921. Minimum Add to Make Parentheses Valid
1021. Remove Outermost Parentheses
1190. Reverse Substrings Between Each Pair of Parentheses
1249. Minimum Remove to Make Valid Parentheses

* Round 2: Dynamic Programming
746. Min Cost Climbing Stairs
931. Minimum Falling Path Sum
935. Knight Dialer
1025. Divisor Game
1155. Number of Dice Rolls With Target Sum

* Round 3: Graph (BFS/DFS)
802. Find Eventual Safe States
818. Race Car
841. Keys and Rooms
842. Split Array into Fibonacci Sequence
1042. Flower Planting With No Adjacent
1129. Shortest Path with Alternating Colors
1136. Parallel Courses

* Round 4: The fourth interview focused on System Design. The problem was the unlike most leetcode questions where there exists a clearly optimal method or strategy to solve the problem (ie. all above examples have a "category" or "flavor" or "type" of problem). This System Design problem really threw me for a loop because I have perfectionist tendencies. The most similiar leetcode problem I could find would be 1247. Minimum Swaps to Make Strings Equal. I looked at this problem for an hour trying to calculate a simple and concise "formula". However, there is no "formula" that I could find. Instead this problem required some unique reasoning. For me, this fourth interview question was by far the hardest interview question since it required similar unique reasoning.

* Round 5: The lunch "interview" was awesome. All food at Google is free, so I chowed down on some amazingly tasty fish and learned more about Google during a casual lunch in the downstairs cafeteria.

* Round 6: The behavioral interview was performed in usual, industry expected manner.

Summary and Advice:

* Don't try to "fake" it. Either you actually know algorithms and data structures XOR you know about algorithms and data structures. This small difference is a huge difference! It is impossible to "fake" algorithmic thinking and understanding. Objective measurement of your individual performance can be derived from weekly leetcode.com contests.

* There are 3 stages to acquire a new skill:

1. Cognitive: focused thought required to perform a task
2. Associative: improved accuracy and efficiency, much less concentration required to perform a task
3. Autonomous: perform task automatically with barely any concious effort at all with optimal accuracy and efficiency

* In order to "pass" the onsite interview, I strongly feel that one needs to be at the autonomous stage for understanding and coding all basic algorithms and data structures. Google provides candidates more than enough preparation material to understand what "basic" means (ie. Trees, Graphs (BFS/DFS/DFS+BT), DP (top-down/bottom-up), Stacks/Queues, Hash Tables, etc.). I estimate studying 10-20% of the preparation material provided by Google a few weeks prior to interviews; it's significant amount of information to "digest" in a short period of time.

* A Rubik's cube can be used as a canonical physical example of autonomous algorithmic understanding. Check out this YouTube video of 2 solutions. An astute observer will notice that I definitely "messed up" a handful of times while solving both the Beginner's Method as well as the Fridrich Method. However, I do not beat myself up about it. We are all human beings, and none of us is perfect. So don't be too hard on yourself, especially when learning something new. Each time I made a mistake, I simply thought, "oops", and resumed the next steps towards a solution the best I could. Always focus on the process towards a solution, not the bumps in the road on your journey there. I'm currently at the autonomous stage for the Beginner's Method, and I'm somewhere between the cognitive/associative stages for the Fridrich Method F2L. I hope that helps provide a better "feel" for what each of those 3 stages mean. Note: A few months after I joined leetcode in 2017 and studied Stefan Pochmann's solutions, I stumbled upon the Old Pochmann Algorithm. And I told myself, "if this fellow can solve a Rubik's cube blindfolded, I can at least learn how to solve it with my eyes open!" (that's easier said than done, if anyone's interested in learning, check this out: https://claytonjwong.github.io/rubiks-cube/).

* Know when to use which data structure and algorithm: Most questions are open-ended and require additional information gathering. Clearly and concisely communicate your thought process while solving the problem. My perfectionist tendencies are to create an elegant solution on the first try. However, all questions asked onsite were non-trivial for which there exists no immediate "perfect" solution. Start off with a "good enough" working solution, then optimize it. There's no sense optimizing an incorrect solution! Start off with basic fundamentals, and incrementally refactor "as needed".

* Be a humble, life-long learner. Never give up! Never surrender!

* There's a lot of information to acquire for simply understanding the fundamentals of algorithms. For example, the CLRS "Intro to Algorithms" book is 1292 pages long; that's a loquacious "introduction"! It takes time to fundamentally understand these algorithms by sharpening the mind's eye. However, the brain can slowly restructure itself to meet cognitive demands. Just learn a little bit each day and stick with it. The compounding interest (ie. pay day) will come. That's the law of the harvest, you reap what you sow.
* Final Thoughts: I really hope this is a helpful and motivational post for everyone, and especially for "older" software engineers like myself. Have fun and keep learning! Continually re-invent yourself as a modern software engineer.


## How to get into FAANG
* Prompt: Suggest the best resources for each topic that Faang interviewer can ask. You may include a few books as well if really needed, but I honestly prefer online resources. Also, I will be happier if you give the one resource recommendations for one topic. If you have two recommendations for some of the topics and you feel that I should go through both, then suggest both.
* URL: https://www.rooftopslushie.com/request/How-to-get-into-FAANG---proper-plan-with-sources-241
* The resources you need are fairly straightforward. I’m going to make this one long post and copy paste the response because you essentially are asking a derivation of each question in each section of your post.
* Instead of simply answering your above post let me give you a rough timeline since you have no prior knowledge. Before Leetcode get 1 book. Go through MOST of Cracking the Coding Interview. I say most because there are sections (like the one on math) that are increasingly less important for CS interviews.
* Follow the entirety of the book taking copious notes and attempting EVERY problem (NO SHORTCUTS!). You can think of the book as essentially your version of taking college level DS and Algo courses. Once you complete the book and problems you will have benefitted twofold:
1. You will have practiced actual interview problems
2. You will have a good framework for your preparation
3. You will have 90% of the fundamentals down for all possible coding problems
4. You should have / will have identified your weaknesses and know where to focus your study.

* Follow the book’s guidelines on soft skills, resume prep, study timeline as well. Use it holistically as it was meant, it is an excellent resource.

* I know you prefer online resources but this book is the most well rounded comprehensive interview prep book (ie it covers a lot of ground relatively succinctly that you will need for interviews, including system design).
* Unfortunately I don’t believe this book is always sufficient prep by itself. So after you work through it your next step is to:
1. Get leetcode premium
2. Take the Grokking the System Design course

* Use Leetcode Premium specifically to do problems that are tagged to companies you are interested in and to do additional practice on areas you are weak at (ie if you suck at Dynamic Programming sort by all top rated DP problems and do them from easiest to hardest to build your intuition).

* Use Grokking the System Design Interview to cover ground not covered in Cracking the Coding Interview (CTCI). CTCI has a lot of great breadth but falls short of depth in some areas, this is one of them.

* Your last step / piece of overarching advice here is to create a timeline of when you would like to interview and work backwards. Once you are starting to seriously think about interviewing it is time to both practice problems for time and to do mock interviews (interviewing.io etc). Do your prep only with a pen / paper and a whiteboard (if that is the medium you expect to be interviewing in) and work on time.

* Once you hit the interviewing stage it is usually time to start scheduling some interviews you aren’t as psyched about for a test run. You need to get used to performing with interview jitters as well.

* So to recap:

* CTCI (maybe 3 months if no prior knowledge) -> Leetcode + Grokking (a month to start shoring things up) -> Keep Leetcoding / Practice + Doing mocks 1/2 times a week (a month) -> assess your progress if you’re ready to start interviewing -> Start doing interviews with lower priority companies -> Schedule interviews with FAANG


=> Google SWE (Blind: teamblind.com/article/Thank-you-Blind-JpZWEdHg)
* Did about 300 LC [20/50/30] (I ended up getting leetcode premium) (about 7 months)
* Some good tips for approaching leetcode: I eased into it with lc easy, put a lot of weight on medium and try to challenge myself with hard. If you can't solve a problem, don't look at the answer. Skip it and work on another one. I'll come back to the question and give it another try. Try to look for hints. If you still can't answer, look at the answer. Come back to the question again a month later and give it another try. Before you look at any answers, always remember to try it first.
* Read Cracking the Coding Interview and Computer Science Distilled. Also took Grokking the System Design Interview course. Watched a ton of cs-related youtube videos in my spare time.
* After getting LC out of the way, I wanted to get an idea of what the criteria was. I foudn a hiring manager on rooftop slushie. They took a look at my resume and gave me a referral. I also got some help regarding the behavioral portion, things like what they're looking for, what qualities I should present, and what kind of personal experiences to bring up.

=> Google SWE (https://www.rooftopslushie.com/request/Google-Onsite-Limit-1202)
=> What's required is practice - lots of it. Coding, system design, leadership.
* Plan for 1-2 months of sincere preparation (2-3 hours every day). About an hour in the morning and an hour in the evening, with larger blocks of time during weekends to take on larger chunks of tasks. I've provided some details on the interview prep for slightly more senior role (L5).
* Coding/problem solving: these are straightforward. You will be presented with a problem and you must think of an approach to solve it, implement code to demonstrate the solution, and reason about its runtime complexity (time and space). The interviewer might add some additional constraints to reason about efficiency or alternative approaches. Your goal is to arrive at the efficient solution and reason about the merits and pitfalls of various approaches along the way. Practicing the medium and hard questions on leetcode (www.leetcode.com) would be helpful here.
* The leadership question will be behavioral and you will be asked how to handle various types of situations like a disengaged teammate or conflicts of opinions etc.
* The system design interview will focus on how design a common use-case, for example a large e-commerce website or a music streaming service. The key is to focus on how to handle the complexities using well known strategies from distributed systems, stream-processing, map-reduce, services, pub-sub etc. You should have practiced enough problems so that common use-cases roll off your memory easily.
* Lastly, the ML interviews will be focused on a machine learning problem. The key here is to show that you grasp the various skills involved in being an ML engineer. This includes:
    * how to frame your objectives (what loss function will you optimize, why?),
    * select the right dataset (what data will you collect to train your model. Why? how to avoid bias and feedback loops. How will you collect labels or ground truth)
    * feature engineering - how will you transform the raw data into a form useful for models (e.g. normalization, missing values, data cleaning, etc)
    * model selection - what model to use for what type of problem and why (boosted decision trees, deep learning, logistic regression, factorization models etc)
    * training, validation and inference - how will the system be setup how will you do validation, how to address train/test skew etc.
    * productionization - how to monitor performance, how to handle problems, what if new model is corrupt or new training batch is incorrect etc.
* There might be a small coding session involved in the ML interview also, e.g. write code for autocomplete functionality on android keyboard.
* Finally, focus on leadership style interview questions. Learn about the company's leadership and culture. Practice talking about your top 3 projects that you accomplished that had measurable impact (you must know the metrics and numbers that measure success) and that you liked to work on. There will be one set of questions from your resume - your most interesting project and what you liked about it. Walk through a challenging project that you delivered, what was the challenge and how did you overcome it? Then there will be a few hypotheticals thrown in to see how you handle those situations (e.g. what if the eng lead of the partner team disagrees with the schedule for the project you're putting together for the team. How would you approach this situation)
* There will be questions around culture fit and your interest in working here. What's your favorite product from the company that you're interviewing? Why? Why do you want to work here? What excites you the most? Where do you see yourself in 5, 10 years? What are your career goals etc.
* Finally, another set of questions around people and communication skills. How will you handle difficult situations. How would you handle conflicts in a cross functional project spanning multiple teams with differing goals and priorities.

=> Google Interview Process (https://www.rooftopslushie.com/request/Google-SWE-Interview-Process-and-Timeline-24)
* The interview process starts with a recruiter reviewing a person's background to decide if it's worth interviewing them, and also what level they should be considered for. This is a process that I don't have any insight into as a SWE. (One thing to note, though, is that this is the only step where a candidate's resume really matters. Beyond this step, interviewers do theoretically have the ability to view a candidate's resume, but it's not supposed to influence the ratings we give, so a lot of interviewers don't even bother reading it).
* The next step is a phone interview. When the phone interview is scheduled, the recruiter will send the candidate a link to a shared Google doc which will be used for the interview. When the interview happens, a SWE will call the candidate on the phone, and ask them one or more algorithms questions, which the candidate should code a solution to in the Google doc. (Typically it's just one question).
* The phone interview is scheduled to be 45 minutes long, and interviewers are supposed to leave around 10 minutes for the candidate to ask questions at the end, so there's usually roughly 35 minutes to solve the coding question(s). Interviewers typically like to ask questions where the optimal solution is feasible to reach within the allotted time, although there is no hard rule about this.
* After the phone interview, the interviewer will submit an interview rating which consists of:
An overall rating for the candidate, which is one of: strong no hire, no hire, lean no hire, lean hire, hire, strong hire.
A short explanation for the overall rating
A 4-point rating & short explanation for each of a few categories like "coding skills", "comprehension and communication", etc. (These changed pretty recently for SWEs, and are slightly different for intern interviews, so I don't remember the exact categories).
Optionally, a 4-point rating & short explanation for more personality-related categories that measure aspects of leadership or "googleyness", which historically most interviewers leave blank. There's recently been a push to be more deliberate about evaluating these, but I'm not aware of the details yet.
A longer document with notes on how the whole interview went
The timeline for an interviewer to submit this feedback is less than 2 business days in most cases.
* After a recruiter receives the feedback from the phone interview, they will decide whether or not to bring the candidate for onsite interviews. (Or, rarely, they will schedule a second phone interview. From what I understand, this mostly happens because the first interviewer screwed up somehow, and isn't really anything to worry about). I don't have insight into how long recruiters usually take at this step.
* When a candidate comes for an onsite interview, a candidate will usually be scheduled for 4 interviews plus a "lunch interview". Usually two interviews, then lunch, then the last two. The only major differences between onsite and phone interviews are that onsites happen on a whiteboard, and interviewers more often use the full 45 minutes to ask the interview questions, since candidates have time to ask their lunch interviewer questions. Onsites are also somewhat more likely to have 2 (easier) questions, instead of just 1, since there is more time. The lunch interviewer does not rate the candidate, and is just there to make small talk and answer questions (though I think this might be different for different roles or something? In any case, it wouldn't be kept a secret if the candidate was being evaluated during lunch).
* The onsite interviewers submit the same style of feedback as phone interviewers. After they have all submitted feedback, the recruiter will decide whether or not to refer the candidate to a hiring committee. A candidate with very little or no positive feedback usually is outright rejected, but people with mixed feedback or better usually go to the hiring committee. I've never been on a hiring committee, so I don't know a lot about what happens at this point, but the high-level summary is that the committee will review all of the phone and onsite interviewers' feedback and use that to issue a hire/no hire decision. Hiring committees might also recommend a hire, but at a lower level than the candidate was evaluated for. Candidates often don't hear back about the hiring committee decision for at least 2 weeks.
* If the committee recommends a hire, then at that point the recruiter will schedule "fit calls" with managers from a few teams, to see if there's mutual interest between the candidate and that manager. (Sometimes this step may happen before the onsite interviews, instead. I don't know what determines this). Fit calls are pretty unstructured, and not really fail-able, in the sense that even if none of the teams you talk to are interested, the recruiter will likely just schedule you with more teams (this may be less true if the fit calls happen before onsite interviews). That said, getting an offer is dependent on matching with a team, so candidates should try to ask good questions and be personable. After matching with a team, a candidate will get an offer. I don't know how the offer amount is determined.

## Amazon Coding Experience (SDE2)
https://leetcode.com/discuss/interview-experience/507025/amazon-sde-2-nyc-feb-2020-offer

Status: MS Electrical Eng. Top 3 School (Canada)
Experience: a bit less than 2 years (in 5G Research mostly)
Location: NYC
Date: Feb 7 2020

Date Applied: Nov 1st 2019
Date of first contact with recruiter: Nov 17th 2019

I spoke with the recruiter, told him a bit about my background. He told me about his team a bit (SCOT - Forecasting). The conversation went pretty well. At the end of the conversation he told me he would send a list of things I needed to review. It included topics which I should focus on: DS & Algo, OOP, System Design, Leadership Principles. It also included resources like leetcode, careercup etc to prepare for the interview. After getting the email, I replied that I would like to take the assessment on the 4th of December and he agreed.

Prep for OA: I already had a pretty solid foundation in DS & Algo & OOP (comp sci minor in undergrad). I started reviewing my class notes and practicing on leetcode. I didn't leetcode prior to that (I only heard of leetcode last May - (yeah I lived under a rock) ). I bought the leetcode premium. My goal was to finish the problems for Amazon. At the beginning it was taking me around 30 mins - 1 hour to solve easy problems. Medium ones 45 mins - 1 hr 30 mins. Hard 3 hr - 4 hrs. I managed to solve most problems under Amazon and the list for Amazon online assessment (https://leetcode.com/discuss/interview-question/344650/Amazon-Online-Assessment-Questions) before the 4th of December (I studied for about 10 - 12 hours).

Prep Outcome: Learnt some new DS & Algo (Trie, Segmented trees, Red black trees, implemented AVL trees). However, I still was not confident in myself that if I was presented with a new problem I'd be able to solve it within the given time (45 mins).

Online Assessment: Dec 4th 2019

Q1: A variation of top n buzzwords (passed 20/21 test cases)
Q2: A variation of zombie in a matrix (passed 19/20 test cases)
I was told that I didn't pass the online assessment. I emailed my recruiter asking him if he could provide me with any feedback and he told me unfortunately he couldn't. But he put my name down in his calender to contact me again in 3-4 months down the line. I told him look if I can't get any feedback then I am not sure on what to improve on as my test cases (except for an edge case) were passing. And if I can't improve then the next time might be the same. He told me he really won't be able to tell me anything more as he the reviewer didn't provide him with any feedback. Long story short, I moved on but after a week later he contacted me again. He told me that after speaking with me, he asked a hiring manager in his team to go over my OA. The hiring manager reviewed it and told me that I am good to go to the next round. He told me that the other reviewer made a mistake somewhere. But anyways since the holidays were approaching I scheduled my phone interview on the 6th of January.

So, I practiced a lot on leetcode during the break. I wanted to really nail my basics and be confident and solve a given problem within the given time. I did all the cards on leetcode (recursion, recusrion II, stacks, BST, Binary Trees, etc..). I also brushed up on my OOP. I was also preparing for my Google phone interview as well. By the time 6th of January came I solved near to 200 problems or so ( a combination of medium and hards mostly leaning more on the medium side). I was pretty confident in myself by that time. I could solve an easy problem within 5 - 10 mins. medium would take me around 10 - 20 mins. Hard would be around 30 - 1 hr. I also spent a couple of days studying the leadership principles and preparing some examples.

Phone Interview:

started off with my background, what I want to do, what I have been working on. lp questions (about 15 mins).
the coding question (can't disclose it) but it was related to quick sort and it's variations. I discussed two possible solutions. Their tradeoffs, time & space complexities. (best case, worst case and on avg.) (about 15 mins)
the interviewer then switched to more lp questions (5 - 7 mins)
I asked him a couple of questions.
Phone Interview Outcome: My recruiter told me that my interviewer really liked my performance and that I would be moving on to the on-site the very same day. The on- site was scheduled on the 7th of February.

Onsite Prep:

DS & Algo & OOP: I started practicing more on leetcode, redid most of the problems I did before (now for every problem that had multiple solutions, I made sure to go over them and understand each of them). I also did some new problems. Total count ~ 230 (mostly medium and hard)

System design prep: Grokking the system design interview + Donne Martin github. Read some papers, watched videos on youtube (microservices).

Leadership Principles - prepared around 4 - 5 examples that I would use for some common questions.

Onsite Interview: (won't be able to disclose the questions asked)

Round 1 - Software Development Manager in SCOT (System Design): Started off with Leadership principle questions (20 mins). Then moved on to the system design question. Spoke about concepts like CDN, Sharding, SQL vs NoSQL, microservices. Didn't follow the direct approach outlined in either grokking the system design or Donne Martin github. But rather improvised. Didn't do any calculation of capacity constraints whatsoever. But spoke about the desing concepts with possible solutions and their tradeoffs and how it could be implemented. I remember my interviewer saying perfect at some point. Overall I thought it went pretty well.

Round 2 - SDE (<3 years of experience): Logical and Maintainable round (OOP): LP questions for the first 20 mins. Then had to design a file system. Seperated the components into different classes and how they would interact. Solved the problem and the follow ups. She asked all the questions she wanted to ask. There were about 10 minutes left. So, I asked her a few questions. We still had a bit of time left after the Q&A.

Round 3 - SDE with 3 years of experience and SDE with 5+ years of experience (Problem Solving): A leetcode hard problem (histograms, rectangles). I gave the brute force approach then a bit more optimized one. Was asked to code the optimized one. Solved it within 20 mins. Since there was still time left he wanted me to further optimize it. Took me about 5 mins to figure it out, my interviewer also came up to the board to help me with it. He gave a small hint after which it seemed pretty easy. Coded that as well. Had time to spare so I asked them a few questions. (I found out later that this round was the bar raiser).

Round 4 - SDE with about 2 years of experience and SDE with around 5 years of experience: (DS & Algo): I looked it up on leetcode, it has variations of medium to hard (think Trie, prefixes). Solved it with time to spare and answered their follow up questions.

Result: Just heard back yesterday from my recruiter that they were going to extend me an offer for SDE - I position (with expectations to be quickly promoted). Even though I was originally interviewing for the SCOT forecasting team but the two interviewers from my bar raiser are also considering to extend an offer for their respective teams (Ad analytics & AWS - ML).

Advice to fellow leetcoders: Part of interviewing is luck as much as I hate to say it but that's the sad reality. Just try your best. Understand a problem and try to see how you can make it better (instead of solving new problems after you have reached a decent number that is). The solution or the discussions are a great way to do that.
