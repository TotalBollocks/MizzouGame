class User < ActiveRecord::Base
  has_secure_password
  has_many :high_scores
  
  validates :username, presence: true, uniqueness: true
  validates :password, presence: true, confirmation: true
  
  def to_s
    username
  end
  
  def can_play
    if last_played 
      last_played + 15.minutes < DateTime.now
    else
      true
    end
  end
  
  def play_time
    time = last_played + 15.minutes
    time.strftime("%l:%M %p")
  end
end
