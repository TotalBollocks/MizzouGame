class HighScore < ActiveRecord::Base
  belongs_to :user
  
  validates :user, presence: true
  validates :score, presence: true
  
  def to_s
    "#{user} scored: #{score}!"
  end
end
