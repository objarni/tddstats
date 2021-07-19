from pytest import approx
from approvaltests import verify

''' SCENARIOS
green paths
2 cykler, lika stora slices:
  användaren klickar förbi 2 hela cykler och sedan exitar,
  med 1.1 sekund i varje mode -->
  Session lasted 6.6 seconds:
  - RED:   33% of time (2.2 seconds)
  - GREEN: 33% of time (2.2 seconds)
  - BLUE:  33% of time (2.2 seconds)

1 cykel, olika stora slices:
  användaren lägger 3 sekunder i varje red, 2 i green, 1 i blue
  Session lasted 6 seconds:
  - RED:   50% of time (3 seconds)
  - GREEN: 34% of time (2 seconds)
  - BLUE:  17% of time (1 seconds)

'''
from tddstats import TDDSession, SessionLog, RED, GREEN, BLUE


def test_2_cycle_same_lengths():
    times = [1.1 * i for i in range(8)]

    def fake_timer():
        t = fake_timer.times[0]
        fake_timer.times = fake_timer.times[1:]
        return t

    fake_timer.times = times

    session = TDDSession(fake_timer)
    for _ in range(7):
        session.click()

    verify(session.report())


def test_1_cycle_different_lengths():
    times = [0, 3, 5, 6]

    def fake_timer():
        t = fake_timer.times[0]
        fake_timer.times = fake_timer.times[1:]
        return t

    fake_timer.times = times

    session = TDDSession(timer=fake_timer)
    session.click()
    session.click()
    session.click()
    session.click()

    verify(session.report())


def test_session_one_switch():
    session_log = SessionLog(start_time=2)
    session_log.switch(time=3)
    assert [(BLUE, 1)] == session_log.get_log()


def test_session_two_switches():
    session_log = SessionLog(start_time=2)
    session_log.switch(time=3)
    session_log.switch(time=5.5)
    assert [(BLUE, 1), (RED, 2.5)] == session_log.get_log()


def test_session_three_switches():
    session_log = SessionLog(start_time=0)
    session_log.switch(time=1)
    session_log.switch(time=2)
    session_log.switch(time=3)
    assert [(BLUE, 1), (RED, 1), (GREEN, 1)] == session_log.get_log()
