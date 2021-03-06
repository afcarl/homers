import pytz

from flask import url_for


et_tz = pytz.timezone('America/New_York')

def serialize_play(play):
    play_time = pytz.utc.localize(play.at)
    play_time = play_time.astimezone(et_tz)

    return {
        'batter': {
            'name': play.batter.get_full_name(),
            'team': play.batter_team,
            'id': play.batter_id,
        },
        'pitcher': {
            'name': play.pitcher.get_full_name(),
            'id': play.pitcher_id,
            'team': play.pitcher_team,
        },
        'title': play.catchy_journalist_title(),
        'url': url_for('view_play', content_id=play.content_id),
        'at': play_time.strftime('%Y-%m-%dT%H:%M:%S%z'),
    }
